import unittest

"""
Write a function that returns an interlaced strings
from two input strings.
s1 = 'abc'; s2 = 'def' --> 'adbecf'
If the length of the strings are different, put the 
leftover characters at the end.
You MUST use the template provided below.
You are not allowed to use explicit loop mechanism.

def interlace_string(s1, s2):
    def helper_interlace_string(s1, s2, out):
        if s1 == '':
            # WRITE ONE LINE OF CODE.
        if s2 == '':
            # WRITE ONE LINE OF CODE.
        else:
            # WRITE ONE LINE OF CODE.
    return helper_interlace_string(s1, s2, '')
"""

class InterlaceStringTest(unittest.TestCase):

    def test_interlace_string(self):
        s1 = 'ace'
        s2 = 'bdf'
        s = 'abcdef'
        self.assertEqual(interlace_string(s1, s2), s)

    def test_interlace_string_diff_length(self):
        s1 = 'acegh'
        s2 = 'bdf'
        s = 'abcdefgh'
        self.assertEqual(interlace_string(s1, s2), s)

    def test_helper_interlace_string_empty(self):
        s1 = 'ace'
        s2 = ''
        s = 'ace'
        self.assertEqual(interlace_string(s1, s2), s)


def interlace_string(s1, s2):
    def helper_interlace_string(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helper_interlace_string(s1[1:], s2[1:], out + s1[0] + s2[0])
    return helper_interlace_string(s1, s2, '')


"""
Write a function to detect if two strings are anagrams or not.
For the sake of simplicity, we will assume that the two strings in question
are of equal length and that they are made up of symbols from the set of
26 lowercase alphabetic characters.
s1: python; s2:typhon areanagrams(s1, s2): True
"""
class AreAnagramsTest(unittest.TestCase):
    def test_are_anagrams(self):
        s1 = 'python'
        s2 = 'typhon'
        self.assertTrue(are_anagrams(s1, s2))

    def test_are_anagrams_palindrome(self):
        s1 = 'madam'
        s2 = 'madam'
        self.assertTrue(are_anagrams(s1, s2))

    def test_are_anagrams_false(self):
        s1 = 'python'
        s2 = 'java'
        self.assertFalse(are_anagrams(s1, s2))

def are_anagrams(s1, s2):
    """
    This program check wheter or not two strings are anagrams.
    It uses a hash table to count the ocurrences of each letter in the strings.
    """
    d1 = dict.fromkeys(list(s1), 0)
    d2 = dict.fromkeys(list(s2), 0)
    for i, j in zip(list(s1), list(s2)):
        d1[i] += 1
        d2[j] += 1
    for key in d1:
        if not d2.has_key(key):
            return False
        if d1[key] != d2[key]:
            return False
    return True

if __name__ == '__main__':
    unittest.main()
