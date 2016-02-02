import random
import unittest

class QuickSortTest(unittest.TestCase):
    def test_quick_sort(self):
        l = [7,5,9,11,6]
        l_sorted = [5,6,7,9,11]
        self.assertListEqual(quick_sort(l), l_sorted)
        self.assertListEqual(quick_sort_randomized(l), l_sorted)

    def test_quick_sort_duplicates(self):
        l = [1,1,1,0,0,0,2]
        l_sorted = [0,0,0,1,1,1,2]
        self.assertListEqual(quick_sort(l), l_sorted)
        self.assertListEqual(quick_sort_randomized(l), l_sorted)

    def test_quick_sort_intercalary(self):
        l = [1,3,2,4,5,7,6,8]
        l_sorted = [1,2,3,4,5,6,7,8]
        self.assertListEqual(quick_sort(l), l_sorted)
        self.assertListEqual(quick_sort_randomized(l), l_sorted)

    def test_quick_sort_single(self):
        l = [999]
        l_sorted = [999]
        self.assertListEqual(quick_sort(l), l_sorted)
        self.assertListEqual(quick_sort_randomized(l), l_sorted)

def quick_sort(x):
    """Sorts an input list using the quick sort algorithm.
       Worst case running time is O(n^2). Expected running time is O(nlgn).
       It does not require extra space --> O(1) space.       
    """
    if len(x) <= 1:
        return x
    pivot = x[0]
    pivot_less, pivot_equal, pivot_greater = [], [], []
    for element in x:
        if element < pivot:
            pivot_less.append(element)
        elif element == pivot:
            pivot_equal.append(element)
        else:
            pivot_greater.append(element)
    return quick_sort(pivot_less) + pivot_equal + quick_sort(pivot_greater)

def quick_sort_randomized(x):
    """Similar to quick_sort method but here the pivot is selected 
       from the list indices uniformly at random.
    """
    if len(x) <= 1:
        return x
    pivot = random.choice(x)
    pivot_less, pivot_equal, pivot_greater = [], [], []
    for element in x:
        if element < pivot:
            pivot_less.append(element)
        elif element == pivot:
            pivot_equal.append(element)
        else:
            pivot_greater.append(element)
    return quick_sort(pivot_less) + pivot_equal + quick_sort(pivot_greater)


if __name__ == '__main__':
    unittest.main()
