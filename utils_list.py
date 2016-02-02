import unittest

"""
Write a function that takes an array of numbers and returns the greatest 
difference you can get by subtracting any two of those numbers.
"""
class MaxDifferenceTest(unittest.TestCase):

    def test_max_difference(self):
        l = [9,10,76,1,34]
        res = 75
        self.assertEqual(max_difference(l), res)

    def test_max_difference_negatives(self):
        l = [1,-2,-5,-999]
        res = 1000 # 1 - (-999)
        self.assertEqual(max_difference(l), res)

    def test_max_difference_duplicates(self):
        l = [1,1,1]
        res = 0
        self.assertEqual(max_difference(l), res)

def max_difference(x):
    """We keep track of the min and max in the same loop.
       Running time: O(n); Space: O(1)
    """
    min_val = x[0]
    max_val = x[0]
    for element in x:
        if element < min_val:
            min_val = element
        elif element > max_val:
            max_val = element
    return max_val - min_val

if __name__ == '__main__':
    unittest.main()
