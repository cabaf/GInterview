import unittest

class MergeSortTest(unittest.TestCase):
    def test_merge_sort(self):
        l = [5, 7, 1, 6, 3]
        l_sorted = [1, 3, 5, 6, 7]
        self.assertListEqual(merge_sort(l), l_sorted)

    def test_merge_sort_duplicates(self):
        l = [1,1,1,1,1,0,0,0,0,0,5]
        l_sorted = [0,0,0,0,0,1,1,1,1,1,5]
        self.assertListEqual(merge_sort(l), l_sorted)

    def test_merge_sort_intercalary(self):
        l = [1,3,5,2,4,6]
        l_sorted = [1,2,3,4,5,6]
        self.assertListEqual(merge_sort(l), l_sorted)

    def test_merge_sort_single(self):
        l = [0]
        l_sorted = [0]
        self.assertListEqual(merge_sort(l), l_sorted)

def merge_sort(x):
    """Sorts an input list in O(nlgn) time.
       It requires O(n) extra space."""
    def merge(x1, x2):
        """Merge two sorted lists into one sorted list.
           Running time: O(n).
        """
        # Fingers pointing to x1 and x2.
        i, j = 0, 0
        merged_list = []
        while True:
            if x1[i] < x2[j]:
                merged_list.append(x1[i])
                i += 1
            else:
                merged_list.append(x2[j])
                j += 1
            if i == len(x1):
                merged_list.extend(x2[j:])
                break
            if j == len(x2):
                merged_list.extend(x1[i:])
                break
        return merged_list
    if len(x) <= 1:
        return x
    middle_index = len(x) / 2
    l1 = merge_sort(x[:middle_index])
    l2 = merge_sort(x[middle_index:])
    return merge(l1, l2)

if __name__ == '__main__':
    unittest.main()
