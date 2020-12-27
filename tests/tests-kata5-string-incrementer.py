import unittest
from incolumepy.codewars.kata5_string_incrementer import increment_string


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(increment_string("foo"), "foo1")
        self.assertEqual(increment_string("foobar001"), "foobar002")
        self.assertEqual(increment_string("foobar1"), "foobar2")
        self.assertEqual(increment_string("foobar00"), "foobar01")
        self.assertEqual(increment_string("foobar99"), "foobar100")
        self.assertEqual(increment_string("foobar099"), "foobar100")
        self.assertEqual(increment_string(""), "1")


if __name__ == '__main__':
    unittest.main()
