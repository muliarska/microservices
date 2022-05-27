import hazelcast
# from hazelcast.client import HazelcastClient
# from hazelcast.config import ClientConfig
import time


# starting Hazelcast Client and connecting it to the running clusters
client = hazelcast.HazelcastClient(cluster_name="dev",
                                   cluster_members=[
                                       # "127.0.0.1:5701",
                                       "127.0.0.1:5702",
                                       "127.0.0.1:5703"
                                   ])
print("Connected to the clusters")


bounded_queue = client.get_queue("my-bounded-queue").blocking()
n = 1000
for i in range(n):
    value = bounded_queue.take()
    if i % 100 == 0:
        print(f"Reading: {value}")
    time.sleep(0.01)


# exit from Hazelcast Client
client.shutdown()
