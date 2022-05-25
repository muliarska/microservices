import hazelcast
import logging
import time


logging.basicConfig(level=logging.INFO)
# starting Hazelcast Client and connecting it to the running clusters
client = hazelcast.HazelcastClient(cluster_name="dev",
                                   cluster_members=[
                                       "127.0.0.1:5701",
                                       "127.0.0.1:5702",
                                       "127.0.0.1:5703"
                                   ])
print("Connected to the clusters")


distributed_map = client.get_map("my-distributed-map")
n = 1000
key = '1'
value = '0'
distributed_map.put_if_absent(key, value)
for i in range(n):
    value = distributed_map.get(key)
    time.sleep(0.01)

    value = str(int(value.result()) + 1)
    distributed_map.put(key, value)

print("Added to the distributed map")
print(f"Result: {distributed_map.get(key).result()}")


# exit from Hazelcast Client
client.shutdown()
