from flask import Flask, request
import requests
from message import Message

app = Flask(__name__)
logging_url = "http://localhost:81/logging"
messages_url = "http://localhost:82/messages"


@app.route("/facade", methods=['GET', 'POST'])
def facade() -> str:
    if request.method == 'POST':
        # receive message from request json
        msg = Message(request.json.get("msg", None))
        # TODO: Add logging.

        # send this message to logging service with POST request
        logging_post_dict = {"text": msg.text(), "uuid": msg.uuid()}
        response = requests.post(logging_url, json=logging_post_dict)

        return response.text

    elif request.method == 'GET':
        # receive all messages from logging service with GET request
        logging_response = requests.get(logging_url).text
        # receive response from messages service with GET request
        messages_response = requests.get(messages_url).text

        # merge and return responses
        return f"Logging service response:\n{logging_response}\nMessages service response:\n{messages_response}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
