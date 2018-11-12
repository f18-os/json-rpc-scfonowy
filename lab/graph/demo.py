from node import *
from json import loads, dumps

leaf1 = Node("leaf1")
leaf2 = Node("leaf2")

root = Node("root", [leaf1, leaf1, leaf2])
encoder = NodeEncoder()
decoder = NodeDecoder()

# print("graph before increment")
# root.show()
# print(encoder.default(root))

# do this increment remotely:
root.increment()

encoded_graph = dumps(encoder.default(root))
Node.all_nodes = {}

print(encoded_graph)

decoded_graph_root = loads(encoded_graph, cls=NodeDecoder)
decoded_graph_root.show()

# print("graph after increment")
# root.show()
# print(encoder.default(root))

