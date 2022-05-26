from flask import Flask, request
import requests
import uuid
from random import choice


app = Flask(__name__)
logging_urls = ["http://localhost:8082/logging", "http://localhost:8083/logging", "http://localhost:8084/logging"]
messages_url = "http://localhost:8081/messages"


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

        # send this message to logging service with POST request
        logging_post_dict = {"text": msg.text(), "uuid": msg.uuid()}
        # select random logging service to work with
        logging_url = choice(logging_urls)
        print(f"Facade service sent message to: {logging_url}")
        response = requests.post(logging_url, json=logging_post_dict)

        return response.text

    elif request.method == 'GET':
        # receive all messages from logging service with GET request
        logging_url = choice(logging_urls)
        logging_response = requests.get(logging_url).text
        # receive response from messages service with GET request
        messages_response = requests.get(messages_url).text

        # merge and return responses
        return f"Logging service response:\n{logging_response}\nMessages service response:\n{messages_response}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
