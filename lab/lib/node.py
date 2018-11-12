from json import JSONEncoder, JSONDecoder, dumps
from threading import local

class Node: # need thread-specific node table for unpacking
    def __init__(self, name, children = None):
        self.name = name
        self.children = children if children != None else []
        self.val = 0

    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)

    def increment(self):
        self.val += 1
        for c in self.children:
            c.increment()
    
# class NodeEncoder(JSONEncoder):
#     def default(self, obj):
#         if (isinstance(obj, Node)):
#             # want to send the table of all nodes to make unpacking easier
#             return {"node_table" : Node.serialize()}
#         else:
#             return JSONEncoder.default(self, obj)

# class NodeDecoder(JSONDecoder):
#     def __init__(self, *args, **kwargs):
#         JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)
    
#     def object_hook(self, obj):
#         if ("node_table" in obj):
#             node_table = obj["node_table"]
#             node_instances = {}

#             for node in node_table: # start by initializing all nodes
#                 node_instances[node["name"]] = Node(node["name"])
#                 node_instances[node["name"]].val = node["val"]
            
#             for node in node_table: # now that all nodes exist, create edges
#                 for child_name in node["children"]:
#                     node_instances[node["name"]].children.append(node_instances[child_name])
            
#             return node_instances["root"] # return root
            
#         return obj

# class NodeNameError(Exception):
#     pass

# class NodeMissingRootError(Exception):
#     pass