import hazelcast
# from hazelcast.client import HazelcastClient
# from hazelcast.config import ClientConfig
import time


# starting Hazelcast Client and connecting it to the running clusters
client = hazelcast.HazelcastClient(cluster_name="dev",
                                   cluster_members=[
                                       "127.0.0.1:5701",
                                       # "127.0.0.1:5702",
                                       # "127.0.0.1:5703"
                                   ])
print("Connected to the clusters")


bounded_queue = client.get_queue("my-bounded-queue").blocking()
n = 1000
for i in range(n):
    bounded_queue.put(f"value-{i}")
    if i % 100 == 0:
        print(f"Writing: value-{i}")
    time.sleep(0.01)


# exit from Hazelcast Client
client.shutdown()
