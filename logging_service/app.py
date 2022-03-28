from flask import Flask, request


app = Flask(__name__)
msgs_map = dict()


@app.route("/logging", methods=['GET', 'POST'])
def logging() -> str:
    if request.method == 'POST':
        # receive message from facade service
        text = request.json.get("text", None)
        uuid = request.json.get("uuid", None)
        print(f"Logging service received message: {text}, with uuid: {uuid}")

        # store this message to local map
        global msgs_map
        msgs_map[uuid] = text

        return ""

    elif request.method == 'GET':
        # return all messages
        msgs = ""
        for value in msgs_map.values():
            msgs += value
            msgs += ", "
        return "[" + msgs[:-2] + "]"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
