from flask import Flask, jsonify, request

app = Flask(__name__)
msgs_map = {}


@app.route("/logging", methods=['GET', 'POST'])
def post_msg() -> str:
    if request.method == 'POST':
        # receive message from facade service
        msg = request.json.get("msg", None)
        uuid = request.json.get("UUID", None)
        print("Received in logging")

        # store this message to local map
        # TODO: change this map to Hash map with multi threads support
        global msgs_map
        msgs_map[uuid] = msg

        # return received message
        return msg

    elif request.method == 'GET':
        # return all messages
        msgs = "All messages:"
        for value in msgs_map.values():
            msgs += "\n"
            msgs += value
        return msgs


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
