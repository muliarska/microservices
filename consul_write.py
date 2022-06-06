import consul

session = consul.Consul()
session.kv.put("hazelcast_ports", "127.0.0.1:5701 127.0.0.1:5702 127.0.0.1:5703")
session.kv.put("my-distributed-map", "map")
session.kv.put("my-bounded-queue", "queue")
