# Basic microservices architecture

Author: [Yana Muliarska](https://github.com/muliarska)

## Usage example

1. Run microservices

Go to the next directories and perform flask app running command:
- facade_service: `flask run -h localhost -p 8080`
- logging_service: `flask run -h localhost -p 8081`
- messages_service: `flask run -h localhost -p 8082`

If you want to change ports, you should change them in the code as well (`logging_url` and `messages_url` in [facade/app.py](https://github.com/muliarska/microservices/blob/micro_basics/facade_service/app.py))

2. Open Postman or another platform for performing requests.

3. `POST http://localhost:8080/facade` with json: `{"msg": "Слава"}`

![post_1](https://github.com/muliarska/microservices/blob/micro_basics/examples/post_1.png)

4. `POST http://localhost:8080/facade` with json: `{"msg": "Україні!"}`

![post_2](https://github.com/muliarska/microservices/blob/micro_basics/examples/post_2.png)

5. `GET http://localhost:8080/facade`

![get](https://github.com/muliarska/microservices/blob/micro_basics/examples/get.png)


## Logs example

In the facade service console you can see simple logs on what is going on:

![facade](https://github.com/muliarska/microservices/blob/micro_basics/examples/facade.png)

Similar logs in logging service console:

![logging](https://github.com/muliarska/microservices/blob/micro_basics/examples/logging_logs.png)

