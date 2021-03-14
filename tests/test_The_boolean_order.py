import unittest
from TestBase import BaseTestCase
from incolumepy.codewars.The_boolean_order import solve

"""
In this Kata, you will be given boolean values and boolean operators.
Your task will be to return the number of arrangements that evaluate to True.

t,f will stand for true, false and the operators will be Boolean AND (&), OR (|), and XOR (^).

For example, solve("tft","^&") = 2, as follows:

    "((t ^ f) & t)" = True
    "(t ^ (f & t))" = True

Notice that the order of the boolean values and operators does not change. What changes is the position of braces.

More examples in the test cases.

Good luck!
"""


class MyTestCase(BaseTestCase):
    def test_something(self):
        """Basic tests"""
        tests = [
            self.t(("tft", "^&"), 2),
            self.t(("ttftff", "|&^&&"), 16),
            self.t(("ttftfftf", "|&^&&||"), 339),
            self.t(("ttftfftft", "|&^&&||^"), 851),
            self.t(("ttftfftftf", "|&^&&||^&"), 2434),
        ]
        for test in tests:
            self.assertEqual(test.expected, solve(*test.entrance))


if __name__ == '__main__':
    unittest.main()
