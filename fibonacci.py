import unittest

class FibTest(unittest.TestCase):
    def test_fib(self):
        n = 7
        res = 13
        self.assertEqual(fib(n), res)

def fib(n):
    if n < 3:
        return 1
    return fib(n -1) + fib(n - 2)

if __name__ == '__main__':
    unittest.main() 
