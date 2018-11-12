#! /usr/bin/env python3

# minimalistic server example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

### NOTE: Code mostly as provided. Only changed what function the ServerServices class exports.
import socket
from lib.graph import Graph, GraphEncoder, GraphDecoder
from json import loads, dumps
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)


# Class providing functions for the client to use:
@service_class
class ServerServices(object):

  @request
  def increment(self, obj):
    encoder = GraphEncoder()
    graph = loads(obj, cls=GraphDecoder)
    graph.increment()
    return dumps(encoder.default(graph))

# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
