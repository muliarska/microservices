# Microservices architecture with Consul

Author: [Yana Muliarska](https://github.com/muliarska)

## Usage example

### 0. Run Consul
`bash consul/start.sh`

To stop the Consul, run `bash consul/stop.sh` in the end.

### 1. Run hazelcast

Install hazelcast, go to the `hazelcast-4.2.5` directory and run `bin/start.sh`

### 2. Run microservices

Go to the next directories and run microservices by commands:
- facade_service: `flask run -h localhost -p 8080` to run facade microservice
- logging_service: `flask run -h localhost -p 8081` to run logging 1 microservice
- logging_service: `flask run -h localhost -p 8082` to run logging 2 microservice
- logging_service: `flask run -h localhost -p 8083` to run logging 3 microservice
- messages_service: `flask run -h localhost -p 8084` to run messages 1 microservice
- messages_service: `flask run -h localhost -p 8085` to run messages 2 microservice

If you want to change ports, you should change them in the code as well (`logging_url` and `messages_url` in [facade/app.py](https://github.com/muliarska/microservices/blob/micro_basics/facade_service/app.py))

### 3. Open Postman or another platform for performing requests.

### 4. Run 10 POST requests to the facade microservice `POST http://localhost:8080/facade` with json: `{"msg": "msg{number}"}` for number in range [1, 10]

![post_request](https://github.com/muliarska/microservices/blob/micro_mq/logs/post_request.png)

Requests work and return "".

### 5. Run GET request to the facade microservice `GET http://localhost:8080/facade`

![get_request](https://github.com/muliarska/microservices/blob/micro_mq/logs/get_request.png)

Request works and return correct messages.

### 6. Here you can see console output for each microservice:

- Facade microservice

![facade_logs](https://github.com/muliarska/microservices/blob/micro_mq/logs/facade_logs.png)

- Logging 1 microservice

![logging_1_logs](https://github.com/muliarska/microservices/blob/micro_mq/logs/logging_1_logs.png)

- Logging 2 microservice

![logging_2_logs](https://github.com/muliarska/microservices/blob/micro_mq/logs/logging_2_logs.png)

- Logging 3 microservice

![logging_3_logs](https://github.com/muliarska/microservices/blob/micro_mq/logs/logging_3_logs.png)

- Messages 1 microservice

![messages_1_logs](https://github.com/muliarska/microservices/blob/micro_mq/logs/messages_1_logs.png)

- Messages 2 microservice

![messages_2_logs](https://github.com/muliarska/microservices/blob/micro_mq/logs/messages_2_logs.png)



