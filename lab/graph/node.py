from json import JSONEncoder, JSONDecoder, dumps

class Node:
    all_nodes = {} # track all nodes to prevent duplicate name error

    def __init__(self, name, children = None):
        if name in Node.all_nodes: # to make life simple, let's not allow multiple nodes of the same name
            raise NodeNameError("Trying to create a node with a name that already exists.")

        self.name = name
        self.children = children if children != None else []
        self.val = 0

        Node.all_nodes[self.name] = self
    
    def __del__(self): # remove name from table upon deletion
        Node.all_nodes.pop(self.name, None)

    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)

    def increment(self):
        self.val += 1
        for c in self.children:
            c.increment()
    
    @staticmethod
    def serialize():
        if "root" not in Node.all_nodes:
            # need to guarantee root node is specified so server can unpack properly
            raise NodeMissingRootError("Attempting to serialize graph with no 'root' node.")

        json_arr = []

        for name, node in Node.all_nodes.items():
            json_arr.append({"name" : name, "val" : node.val, "children" : [c.name for c in node.children]})

        return json_arr
    
    # def serialize(self):
    #     return {"__type__" : self.__class__.__name__, "name" : self.name, "value" : self.val, "children" : [c.serialize() for c in self.children]}
    

class NodeEncoder(JSONEncoder):
    def default(self, obj):
        if (isinstance(obj, Node)):
            # want to send the table of all nodes to make unpacking easier
            return {"node_table" : Node.serialize()}
        else:
            return JSONEncoder.default(self, obj)

class NodeDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):
        JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)
    
    def object_hook(self, obj):
        if ("node_table" in obj):
            node_table = obj["node_table"]
            node_instances = {}

            for node in node_table: # start by initializing all nodes
                node_instances[node["name"]] = Node(node["name"])
                node_instances[node["name"]].val = node["val"]
            
            for node in node_table: # now that all nodes exist, create edges
                for child_name in node["children"]:
                    node_instances[node["name"]].children.append(node_instances[child_name])
            
            return node_instances["root"] # return root
            
        return obj

class NodeNameError(Exception):
    pass

class NodeMissingRootError(Exception):
    pass