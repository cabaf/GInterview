import unittest

class FindValueTest(unittest.TestCase):
    
    def test_find_value(self):
        l = [1,5,9,15,37]
        val = 37
        index = 4
        self.assertEqual(find_value(l, val), index)

    def test_find_value_duplicates(self):
        l = [1,1,5,7,9,590]
        val = 1
        index = [0, 1]
        self.assertIn(find_value(l, val), index)

    def test_find_value_single(self):
        l = [1]
        val = 1
        index = 0
        self.assertEqual(find_value(l, val), index)

    def test_find_value_not_found(self):
        l = [1,2,3]
        val = 333
        self.assertIsNone(find_value(l, val))

def find_value(x_sorted, val):
    """Search for a given value in a sorted list of integers using 
       Binary Search. Running time: O(lgn); In place.
       Args:
           x_sorted: Sorted list.
           val: Value to find.
       Returns:
           index: None if not found. Index of the value in the list.
    """
    if x_sorted:
        half_index = len(x_sorted) / 2
        if val == x_sorted[half_index]:
            return half_index
        elif len(x_sorted) == 1:
            return
        elif val < x_sorted[half_index]:
            index = find_value(x_sorted[:half_index], val)
            shift_index = 0
        elif val > x_sorted[half_index]:
            index = find_value(x_sorted[half_index:], val)
            shift_index = half_index
        if index:
            return index + shift_index

if __name__ == '__main__':
    unittest.main()
