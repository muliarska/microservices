from flask import Flask, request
import hazelcast
import consul
from uuid import uuid4
import argparse


app = Flask(__name__)

# argument parsing for finding ports
parser = argparse.ArgumentParser(description='Parsing port.')
parser.add_argument('--port', type=int)
args = parser.parse_args()
port = args.port

# consul set up
session = consul.Consul(host='localhost', port=8500)
# uuid_numb = uuid4()
session.agent.service.register('logging-service',
                               port=port,
                               service_id=f"logging-{uuid4()}")

# starting Hazelcast Client and connecting it to the running clusters
client = hazelcast.HazelcastClient(cluster_name="dev",
                                   cluster_members=session.kv.get('hazelcast_ports')[1]['Value'].decode(
                                       "utf-8").split())
print("Connected to the clusters")
distributed_map = client.get_map(session.kv.get('my-distributed-map')[1]['Value'].decode("utf-8")).blocking()


@app.route("/logging", methods=['GET', 'POST'])
def logging() -> str:
    if request.method == 'POST':
        # receive message from facade service
        text = request.json.get("text", None)
        uuid = request.json.get("uuid", None)
        print(f"Logging service received message: {text}, with uuid: {uuid}")

        # store this message to the distributed map
        distributed_map.lock(uuid)
        try:
            distributed_map.put(uuid, text)
        finally:
            distributed_map.unlock(uuid)

        # exit from Hazelcast Client
        client.shutdown()
        return ""

    elif request.method == 'GET':
        # return all messages
        msgs = ""
        for value in distributed_map.values():
            msgs += value
            msgs += ", "

        # exit from Hazelcast Client
        client.shutdown()
        return "[" + msgs[:-2] + "]"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
    # app.run(host='0.0.0.0', port=8082)
    # app.run(host='0.0.0.0', port=8083)
