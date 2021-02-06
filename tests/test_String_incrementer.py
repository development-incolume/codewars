import unittest
from incolumepy.codewars.String_incrementer import increment_string
from collections import namedtuple


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.t = namedtuple('test', 'entrance expected')

    @classmethod
    def tearDownClass(cls):
        ...

    def test_basics0(self):
        tests = [
            self.t("foo0", "foo1"),
            self.t("foobar1", "foobar2"),
            self.t("foobar00", "foobar01"),
            self.t("foobar001", "foobar002"),
        ]
        for i in tests:
            self.assertEqual(i.expected, increment_string(i.entrance))

    def test_basics1(self):
        tests = [
            self.t(None, '1'),
            self.t("", "1"),
            self.t("0", "1"),
            self.t('1', '2'),
            self.t('009', '010')
        ]
        for i in tests:
            self.assertEqual(i.expected, increment_string(i.entrance))

    def test_mediums(self):
        tests = [
            self.t("foo", "foo1"),
            self.t("foobar9", "foobar10"),
            self.t("foobar99", "foobar100"),
            self.t("foobar009", "foobar010"),
            self.t("foobar099", "foobar100"),
            self.t('foo899999', 'foo900000')
        ]
        for i in tests:
            self.assertEqual(i.expected, increment_string(i.entrance))

    def test_advanced(self):
        tests = [
            self.t(
              '4Hr>ei4523LkO,+z397027080*%+2:T[502233dt%OC%=#557523Ku5n_25136474lR9~A9279M2827104N]'
              'aWI10419070000045670589',
              '4Hr>ei4523LkO,+z397027080*%+2:T[502233dt%OC%=#557523Ku5n_25136474lR9~A9279M2827104N]'
              'aWI10419070000045670590'
            ),
            self.t('6(L1633235169', '6(L1633235170'),
            self.t("q.~2871332009", "q.~2871332010"),
            self.t('J.Z9l07816203>^jEG{|jb839460@s_ Cm"9550009', 'J.Z9l07816203>^jEG{|jb839460@s_ Cm"9550010'),
            self.t('"4On}Mb0077150000282689', '"4On}Mb0077150000282690'),
            self.t('.%~h9087Yv~3t3<<424371 5AA~b?94j&y022527500000000359',
              '.%~h9087Yv~3t3<<424371 5AA~b?94j&y022527500000000360'),
            self.t("qE7yOPr!71726313\"0/:.(H1.#R3066`^'Nz[r>t4186675470008615188699",
              "qE7yOPr!71726313\"0/:.(H1.#R3066`^'Nz[r>t4186675470008615188700"),
        ]
        for i in tests:
            self.assertEqual(i.expected, increment_string(i.entrance))


if __name__ == '__main__':
    unittest.main()
