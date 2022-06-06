from flask import Flask, request
import requests
import uuid
from random import choice
import hazelcast

import consul
import argparse


app = Flask(__name__)

# argument parsing for finding ports
parser = argparse.ArgumentParser(description='Parsing port')
parser.add_argument('--port', type=int)
args = parser.parse_args()
port = args.port

# consul set up
session = consul.Consul(host='localhost', port=8500)
session.agent.service.register('facade-service',
                               port=port,
                               service_id=f"facade-{str(uuid.uuid4())}")

# Find ports of other services
agent = session.agent
services = agent.services()

# finding logging and messages services urls
logging_urls = []
messages_urls = []
print(services.items())

for key, value in services.items():
    # print(key)
    # print(value)
    service_name = key.split("-")[0]
    if service_name == "logging":
        logging_urls.append(f"http://localhost:{value['Port']}/logging")
    elif service_name == "messages":
        messages_urls.append(f"http://localhost:{value['Port']}/messages")

# starting Hazelcast Client and connecting it to the running clusters
client = hazelcast.HazelcastClient(cluster_name="dev",
                                   cluster_members=session.kv.get('hazelcast_ports')[1]['Value'].decode(
                                       "utf-8").split()
                                   )
print("Connected to the clusters")
bounded_queue = client.get_queue(session.kv.get('my-bounded-queue')[1]['Value'].decode("utf-8")).blocking()


class Message:
    def __init__(self, text):
        self._text = text
        self._uuid = str(uuid.uuid1())

    def text(self):
        return self._text

    def uuid(self):
        return self._uuid


@app.route("/facade", methods=['GET', 'POST'])
def facade() -> str:
    if request.method == 'POST':
        # receive message from request json
        msg = Message(request.json.get("msg", None))
        print(f"Facade service received message: {msg.text()}")

        # LOGGING SERVICE
        # send this message to logging service with POST request
        logging_post_dict = {"text": msg.text(), "uuid": msg.uuid()}
        # select random logging service to work with
        logging_url = choice(logging_urls)
        print(f"Facade service sent message to: {logging_url}")
        response = requests.post(logging_url, json=logging_post_dict)

        # MESSAGES SERVICE
        bounded_queue.put(f"{request.get_json()}")

        return response.text

    elif request.method == 'GET':
        # receive all messages from logging service with GET request
        logging_url = choice(logging_urls)
        logging_response = requests.get(logging_url).text

        # receive response from messages service with GET request
        messages_url = choice(messages_urls)
        messages_response = requests.get(messages_url).text

        # merge and return responses
        return f"Logging service response:\n{logging_response}\nMessages service response:\n{messages_response}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
