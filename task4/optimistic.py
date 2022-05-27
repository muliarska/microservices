import hazelcast
import time


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
key = '1'
value = '0'
distributed_map.put_if_absent(key, value)
for i in range(n):
    while True:
        value = distributed_map.get(key)
        new_value = int(value)
        time.sleep(0.01)

        new_value += 1
        if distributed_map.replace_if_same(key, value, str(new_value)):
            break

print("Added to the distributed map")
print(f"Result: {distributed_map.get(key)}")


# exit from Hazelcast Client
client.shutdown()
