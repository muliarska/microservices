# Microservices architecture with Hazelcast

Author: [Yana Muliarska](https://github.com/muliarska)

## Usage example

### 1. Run microservices

Go to the next directories and run microservices by commands:
- facade_service: `flask run -h localhost -p 8080` to run facade microservice
- messages_service: `flask run -h localhost -p 8081` to run messages microservice
- logging_service: `flask run -h localhost -p 8082` to run logging 1 microservice
- logging_service: `flask run -h localhost -p 8083` to run logging 2 microservice
- logging_service: `flask run -h localhost -p 8084` to run logging 3 microservice

If you want to change ports, you should change them in the code as well (`logging_url` and `messages_url` in [facade/app.py](https://github.com/muliarska/microservices/blob/micro_basics/facade_service/app.py))

### 2. Hazelcast nodes starting

Console log:

![nodes_start](https://github.com/muliarska/microservices/blob/micro_hazelcast/logs/nodes_start.png)

### 3. Open Postman or another platform for performing requests.

### 4. Run 10 POST requests to the facade microservice `POST http://localhost:8080/facade` with json: `{"msg": "msg{number}"}` for number in range [1, 10]

![post_request](https://github.com/muliarska/microservices/blob/micro_hazelcast/logs/post_request.png)

Requests work and return "".

Here we can see logs in the facade microservice console:

![post_facade_log](https://github.com/muliarska/microservices/blob/micro_hazelcast/logs/post_facade_log.png)

Logs in the logging microservice console:

![post_logging_log](https://github.com/muliarska/microservices/blob/micro_hazelcast/logs/post_logging_log.png)

### 5. Run GET request to the facade microservice `GET http://localhost:8080/facade`

![get_request](https://github.com/muliarska/microservices/blob/micro_hazelcast/logs/get_request.png)

Request works and return correct messages.

When removing some Hazelcast nodes, GET requests are still working:

![get_log](https://github.com/muliarska/microservices/blob/micro_hazelcast/logs/get_log.png)

