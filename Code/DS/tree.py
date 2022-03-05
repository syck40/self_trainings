class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None

    def insert_node(self, val):
        if not self.root:
            self.root = Node(val)
        elif self.root.val < val:
            self.insert_node(self.root.right, val)
        else:
            self.insert_node
