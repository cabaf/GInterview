class BSTNode(object):
    def __init__(self, parent, k):
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, k):
        if k == self.key:
            return self
        elif k < self.key:
            if self.left is not None:
                self.left.find(k)
            else:
                return None
        else:
            if self.right is not None:
                self.right.find(k)
            else:
                return None

    def find_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current

    def next_smaller(self):
        if self.left is not None:
             current.left.find_max()
        current = self
        while current.parent is not None and current is current.parent.left:
            current = current.parent
        return current.parent

    def next_larger(self):
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent        

    def insert(self, node):
        if node is None:
            return
        if node.key == self.key:
            return
        if node.key < self.key:
            if self.left is not None:
                self.left.insert(node)
            else:
                node.parent = self
                self.left = node
        else:
            if self.right is not None:
                self.right.insert(node)
            else:
                node.parent = self
                self.right = node

    def find_min(self):
        current = self
        while current.left is not None:
            current = self.left
        return current


class BST(object):
    def __init__(self, klass=BSTNode):
        self.root = None
        self.klass = klass

    def find(self, k):
        return self.root and self.root.find(k)

    def find_min(self):
        return self.root and self.root.find_min()

    def find_max(self):
        return self.root and self.root.find_max()

    def next_smaller(self, k):
        node = self.find(k)
        return node and node.next_smaller()

    def next_larger(self, k):
        node = self.find(k)
        return node and node.next_larger()

    def insert(self, k):
        node = self.klass(None, k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        return node
