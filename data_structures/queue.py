import unittest

class QueueTest(unittest.TestCase):
    def test_Queue(self):
        Q = Queue()
        Q.enqueue(1)
        Q.enqueue(2)
        self.assertEqual(Q.dequeue(), 1)

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isempty(self):
        if self.items:
            return False
        else:
            return True

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    unittest.main()
