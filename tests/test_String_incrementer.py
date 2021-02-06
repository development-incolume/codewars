import unittest
from incolumepy.codewars.String_incrementer import increment_string
from collections import namedtuple


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(increment_string("foo"), "foo1")
        self.assertEqual(increment_string("foobar001"), "foobar002")
        self.assertEqual(increment_string("foobar1"), "foobar2")
        self.assertEqual(increment_string("foobar00"), "foobar01")
        self.assertEqual(increment_string("foobar99"), "foobar100")
        self.assertEqual(increment_string("foobar099"), "foobar100")

    def test_advanced0(self):
        self.assertEqual(increment_string(""), "1")

    def test_advanced1(self):
        self.assertEqual(increment_string(None), '1')

    def test_advanced2(self):
        self.assertEqual(increment_string('1'), '2')

    def test_advanced3(self):
        self.assertEqual(increment_string("q.~2871332009"), "q.~2871332010")

    def test_advanced4(self):
        t = namedtuple('test', 'entrance expected')
        tests = [
            t('J.Z9l07816203>^jEG{|jb839460@s_ Cm"9550009', 'J.Z9l07816203>^jEG{|jb839460@s_ Cm"9550010'),
            t('"4On}Mb0077150000282689', '"4On}Mb0077150000282690'),
            t('.%~h9087Yv~3t3<<424371 5AA~b?94j&y022527500000000359',
              '.%~h9087Yv~3t3<<424371 5AA~b?94j&y022527500000000360'),
            t("qE7yOPr!71726313\"0/:.(H1.#R3066`^'Nz[r>t4186675470008615188699",
              "qE7yOPr!71726313\"0/:.(H1.#R3066`^'Nz[r>t4186675470008615188700"),
        ]
        for i in tests:
            self.assertEqual(increment_string(i.entrance), i.expected)


if __name__ == '__main__':
    unittest.main()
