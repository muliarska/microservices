import hazelcast
# from hazelcast.client import HazelcastClient
# from hazelcast.config import ClientConfig
import logging


logging.basicConfig(level=logging.INFO)
# starting Hazelcast Client and connecting it to the running clusters
client = hazelcast.HazelcastClient(cluster_name="dev",
                                   cluster_members=[
                                       "127.0.0.1:5701",
                                       "127.0.0.1:5702",
                                       "127.0.0.1:5703"
                                   ])
print("Connected to the clusters")


distributed_map = client.get_map("my-distributed-map").blocking()
n = 1000
for i in range(n):
    distributed_map.put(f"key-{i}", f"value-{i}")
print("Added to the distributed map")


# exit from Hazelcast Client
client.shutdown()
