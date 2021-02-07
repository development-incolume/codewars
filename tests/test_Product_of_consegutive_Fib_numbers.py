import unittest
from TestBase import BaseTestCase
from incolumepy.codewars.Product_of_consecutive_Fib_numbers import productFib, fib, fibonacci


class MyTestCase(BaseTestCase):
    def test_fib(self):
        tests = [
            self.t(-1, 1),
            self.t(0, 1),
            self.t(1, 1),
            self.t(2, 1),
            self.t(5, 5),
            self.t(10, 55),
            self.t(11, 89),
        ]
        for test in tests:
            self.assertEqual(test.expected, fib(test.entrance))

    def test_fibonacci(self):
        tests = [
            self.t(10, 55),
            self.t(2, 1),
            self.t(1, 1),
            # self.t(0, 1),
            # self.t(-1, 1),
        ]
        for test in tests:
            self.assertEqual(test.expected, fibonacci(test.entrance))

    def test_basics(self):
        tests = [
            self.t(4895, [55, 89, True]),
            self.t(5895, [89, 144, False]),
            self.t(0, [-1, 0, False]),
            self.t(0, [0, 1, True]),
        ]
        for test in tests:
            self.assertEqual(test.expected, productFib(test.entrance))


if __name__ == '__main__':
    unittest.main()
