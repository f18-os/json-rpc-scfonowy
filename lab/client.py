# minimalistic client example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

### NOTE: Connection/socket code mostly as provided. Added code to serve as a demo for graph incrementing.
import socket
from lib.graph import Graph, GraphEncoder, GraphDecoder
from json import loads, dumps
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()

graph = Graph()
graph.add_node("leaf1")
graph.add_node("leaf2")
graph.add_node("root", [graph.nodes["leaf1"], graph.nodes["leaf2"], graph.nodes["leaf1"]])

encoder = GraphEncoder()

# Execute in server:
result = loads(server.increment(dumps(encoder.default(graph))), cls=GraphDecoder)
result.nodes["root"].show()

result = loads(server.increment(dumps(encoder.default(result))), cls=GraphDecoder)
result.nodes["root"].show()

rpc.close() # Closes the socket 's' also


