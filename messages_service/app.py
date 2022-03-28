from flask import Flask, request


app = Flask(__name__)


@app.route("/messages", methods=['GET'])
def messages() -> str:
    if request.method == 'GET':
        return "Not implemented yet"
    return f"{request.method} method is not supported"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
