import unittest

from stack import Stack
"""
Check wheter or not parenthesis are balanced.
"""
class BalanceChecker(unittest.TestCase):
    def test_balance_checker(self):
        s = '((()))'
        self.assertTrue(balance_checker(s))

    def test_balance_checker_false(self):
        s = '(((())'
        self.assertFalse(balance_checker(s))

def balance_checker(s):
    balance_weighter = [Stack(), Stack()]
    stack_pointer = 0
    balance_weighter[stack_pointer].push(s[0])
    for e in s[1:]:
        if balance_weighter[stack_pointer].peek() != e:
            stack_pointer = abs(stack_pointer - 1)
            balance_weighter[stack_pointer].push(e)
        else:
            balance_weighter[stack_pointer].push(e)
    if balance_weighter[0].size() != balance_weighter[1].size():
        return False
    return True

if __name__ == '__main__':
    unittest.main()
