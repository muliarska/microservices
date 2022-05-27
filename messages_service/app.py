from flask import Flask, request
import hazelcast


app = Flask(__name__)
messages_list = []


@app.route("/messages", methods=['GET'])
def messages() -> str:
    global messages_list
    # starting Hazelcast Client and connecting it to the running clusters
    client = hazelcast.HazelcastClient(cluster_name="dev",
                                       cluster_members=[
                                           # "127.0.0.1:5701",
                                           "127.0.0.1:5702",
                                           "127.0.0.1:5703"
                                       ])
    print("Connected to the clusters")

    bounded_queue = client.get_queue("my-bounded-queue").blocking()

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
