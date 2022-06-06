from flask import Flask, request
import hazelcast
import consul
import argparse
import uuid


app = Flask(__name__)
messages_list = []

# argument parsing for finding ports
parser = argparse.ArgumentParser(description='Parsing port.')
parser.add_argument('--port', type=int)
args = parser.parse_args()
port = args.port

# consul set up
session = consul.Consul(host='localhost', port=8500)
session.agent.service.register('messages-service',
                               port=port,
                               service_id=f"messages-{uuid.uuid4()}")

# starting Hazelcast Client and connecting it to the running clusters
client = hazelcast.HazelcastClient(cluster_name="dev",
                                   cluster_members=session.kv.get('hazelcast_ports')[1]['Value'].decode(
                                       "utf-8").split())
print("Connected to the clusters")
bounded_queue = client.get_queue(session.kv.get('my-bounded-queue')[1]['Value'].decode("utf-8")).blocking()


@app.route("/messages", methods=['GET'])
def messages() -> str:
    global messages_list

    if request.method == 'GET':
        is_empty = bounded_queue.is_empty()

        while not is_empty:
            text = bounded_queue.take()
            print(f"Messages service received message: {text}")
            messages_list.append(text)

            is_empty = bounded_queue.is_empty()

        # return all messages
        msgs = ""
        for value in messages_list:
            msgs += value
            msgs += ", "

        return "[" + msgs[:-2] + "]"

    return f"{request.method} method is not supported"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8084)
    # app.run(host='0.0.0.0', port=8085)
