import unittest
from incolumepy.codewars.The_boolean_order import solve


class MyTestCase(unittest.TestCase):
    def test_something(self):
        """Basic tests"""
        self.assertEqual(solve("tft", "^&"), 2)
        self.assertEqual(solve("ttftff", "|&^&&"), 16)
        self.assertEqual(solve("ttftfftf", "|&^&&||"), 339)
        self.assertEqual(solve("ttftfftft", "|&^&&||^"), 851)
        self.assertEqual(solve("ttftfftftf", "|&^&&||^&"), 2434)


if __name__ == '__main__':
    unittest.main()
