from lib.node import Node
from json import JSONDecoder, JSONEncoder

### 
#   Graph class that serves as a collection of nodes, largely to enforce
#   that no graph should have more than one node with a name (i.e. in each graph
#   a node's name uniquely identifies either one node or no nodes.)
###
class Graph:
    def __init__(self, root = None):
        self.nodes = {} # used to prevent duplicate node names + for easy serialization
    
    def add_node(self, node_name, children = None):
        if node_name in self.nodes:
            raise GraphDuplicateNodeNameError("Attempting to create a duplicately-named node in the same graph.")
        
        self.nodes[node_name] = Node(node_name, children)
    
    def serialize(self):
        if "root" not in self.nodes:
            # need to guarantee root node is specified so server can unpack properly
            raise GraphMissingRootError("Attempting to serialize graph with no 'root' node.")

        json_arr = []

        for name, node in self.nodes.items():
            json_arr.append({"name" : name, "val" : node.val, "children" : [c.name for c in node.children]})

        return json_arr
    
    def increment(self):
        self.nodes["root"].increment()

###
#   JSON encoding class for Graphs.
###
class GraphEncoder(JSONEncoder):
    def default(self, obj):
        if (isinstance(obj, Graph)):
            # want to send the table of all nodes to make unpacking easier
            return {"graph" : obj.serialize()}
        else:
            return JSONEncoder.default(self, obj)

###
#  JSON decoding class for Graphs.
###
class GraphDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):
        JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)
    
    def object_hook(self, obj):
        if ("graph" in obj):
            graph_dict = obj["graph"]
            graph = Graph()

            for node in graph_dict: # start by initializing all nodes
                graph.add_node(node["name"])
                graph.nodes[node["name"]].val = node["val"]
            
            for node in graph_dict: # now that all nodes exist, create edges
                for child_name in node["children"]:
                    graph.nodes[node["name"]].children.append(graph.nodes[child_name])
            
            return graph # return root
            
        return obj

### Some custom exceptions, to feel fancy when we mess up.
class GraphMissingRootError(Exception):
    pass

class GraphDuplicateNodeNameError(Exception):
    pass