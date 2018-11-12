### NOTE: Node class provided by Dr. Freudenthal with minimal bug-fixing.
class Node: 
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