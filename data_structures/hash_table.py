import unittest

class HashTableTest(unittest.TestCase):
    def test_HashTable(self):
        d = HashTable()
        for i in range(0, 41, 2):
            d.add_item(i)
        self.assertTrue(d.find_item(10))
        self.assertFalse(d.find_item(1))

class HashTable(object):
    def __init__(self, slots=10):
        self.slots = slots
        self.table = []
        self.create_table()

    def create_table(self):
        for e in range(self.slots):
            self.table.append([])

    def add_item(self, item):
        key = self.hash_key(item)
        self.table[key].append(item)

    def hash_key(self, val):
        return hash(val)%self.slots

    def find_item(self, item):
        key = self.hash_key(item)
        return item in self.table[key]

if __name__ == '__main__':
    unittest.main()
