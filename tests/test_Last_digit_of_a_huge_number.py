import unittest
from TestBase import BaseTestCase
from incolumepy.codewars.Last_digit_of_a_huge_number import last_digit


class MyTestCase(BaseTestCase):
    def test_basics(self):
        tests = [
            self.t([], 1),
            self.t([0, 0], 1),
            self.t([0, 0, 0], 0),
            self.t([2, 2, 2, 0], 4),
            self.t([1, 2], 1),
            self.t([3, 4, 5], 1),
            self.t([4, 3, 6], 4),
            self.t([4, 3, 11], 4),
        ]
        for test in tests:
            self.assertEqual(test.expected, last_digit(test.entrance))

    def test_mediums(self):
        tests = [
            self.t([7, 6, 21], 1),
            # self.t([2, 2, 101, 2], 6),
            # self.t([12, 30, 21], 6),
            self.t([937640, 767456, 981242], 0),
            self.t([123232, 694022, 140249], 6),
            self.t([499942, 898102, 846073], 6)
        ]
        for test in tests:
            self.assertEqual(test.expected, last_digit(test.entrance))


if __name__ == '__main__':
    unittest.main()
