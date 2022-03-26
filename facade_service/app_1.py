from flask import Flask, request
import requests
import uuid

app = Flask(__name__)


@app.route("/facade", methods=['GET', 'POST'])
def facade() -> str:
    if request.method == 'POST':
        # receive message from request json
        msg = request.json.get("msg", None)
        print("Received in facade")

        # send this message to logging service with POST request
        logging_post_dict = {"msg": msg, "UUID": str(uuid.uuid1())}
        response = requests.post("http://192.168.1.166:81/logging", json=logging_post_dict)

        # return logging service response (same message)
        return response.text

    elif request.method == 'GET':
        # receive all messages from logging service with GET request
        response = requests.get("http://192.168.1.166:81/logging")
        return response.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
