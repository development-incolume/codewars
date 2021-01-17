import unittest
from incolumepy.codewars.String_incrementer import increment_string


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(increment_string("foo"), "foo1")
        self.assertEqual(increment_string("foobar001"), "foobar002")
        self.assertEqual(increment_string("foobar1"), "foobar2")
        self.assertEqual(increment_string("foobar00"), "foobar01")
        self.assertEqual(increment_string("foobar99"), "foobar100")
        self.assertEqual(increment_string("foobar099"), "foobar100")

    def test_avanced0(self):
        self.assertEqual(increment_string(""), "1")

    def test_avanced1(self):
        self.assertEqual(increment_string(None), '1')

    def test_avanced2(self):
        self.assertEqual(increment_string('1'), '2')

    def test_avanced3(self):
        self.assertEqual(increment_string("q.~2871332009"), "q.~2871332010")

    def test_avanced4(self):
        self.assertEqual(
            increment_string('J.Z9l07816203>^jEG{|jb839460@s_ Cm"9550009'),
            'J.Z9l07816203>^jEG{|jb839460@s_ Cm"9550010')


if __name__ == '__main__':
    unittest.main()
