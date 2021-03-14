import unittest
from incolumepy.codewars.kyu4_Range_Extraction import solution
from TestBase import BaseTestCase


class MyTestCase(BaseTestCase):
    def test_basic(self):
        tests = [
            self.t(
                [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
                '-6,-3-1,3-5,7-11,14,15,17-20'
            ),
            self.t(
                [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20],
                '-3--1,2,10,15,16,18-20'
            ),
        ]
        for test in tests:
            self.assertEqual(solution(test.entrance), test.expected)


if __name__ == '__main__':
    unittest.main()
