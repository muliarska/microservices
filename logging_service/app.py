from flask import Flask, request
import hazelcast


app = Flask(__name__)
# msgs_map = dict()


@app.route("/logging", methods=['GET', 'POST'])
def logging() -> str:

    # starting Hazelcast Client and connecting it to the running clusters
    client = hazelcast.HazelcastClient(cluster_name="dev",
                                       cluster_members=[
                                           "127.0.0.1:5701",
                                           "127.0.0.1:5702",
                                           "127.0.0.1:5703"
                                       ])
    print("Connected to the clusters")

    distributed_map = client.get_map("my-distributed-map").blocking()

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
