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

if __name__ == '__main__':
    unittest.main()
