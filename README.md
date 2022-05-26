# Hazelcast usage

Author: [Yana Muliarska](https://github.com/muliarska)

## Tasks

### 1. I installed and set up [Hazelcast](http://hazelcast.org/download/ )


### 2. Configured and run 3 nodes
Three nodes are connected between each other. Here you can see the console output of one of the nodes:

![nodes_creation](https://github.com/muliarska/microservices/blob/hazelcast_usage/logs/nodes_creation.png)

### 3. Distributed Map usage
Code for this task you can fing in [task3](https://github.com/muliarska/microservices/tree/hazelcast_usage/task3) folder.

Here you can see the output of the console after adding items to the distributed map.
When there are three nodes, the data are distributed almost uniformly. About 330 in each. If you delete one node, the distribution will be about 500 and 500. I did not observe data loss.

![task3](https://github.com/muliarska/microservices/blob/hazelcast_usage/logs/task3.png)

### 4. Distributed Map with locks
Code for this task you can fing in [task4](https://github.com/muliarska/microservices/tree/hazelcast_usage/task4) folder.

Here you can see the console output for different types of locks.

**Without locks**

![no_blocking](https://github.com/muliarska/microservices/blob/hazelcast_usage/logs/no_blocking.png)

**With pessimistic lock**

![pessimistic](https://github.com/muliarska/microservices/blob/hazelcast_usage/logs/pessimistic.png)

**With optimistic lock**

![optimistic](https://github.com/muliarska/microservices/blob/hazelcast_usage/logs/optimistic.png)

### 5. Bounded queue usage for read/write
Code for this task you can fing in [task5](https://github.com/muliarska/microservices/tree/hazelcast_usage/task3) folder.

Here you can see the console output when writing from one node.

![writing](https://github.com/muliarska/microservices/blob/hazelcast_usage/logs/writing.png)

And from two nodes there is a reading.

![reading](https://github.com/muliarska/microservices/blob/hazelcast_usage/logs/reading.png)


