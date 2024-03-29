class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isempty(self):
        if self.items:
            return False
        return True

    def size(self):
        return len(self.items)
