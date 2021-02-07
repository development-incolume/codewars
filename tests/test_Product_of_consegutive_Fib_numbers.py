import unittest
from TestBase import BaseTestCase
from incolumepy.codewars.Product_of_consecutive_Fib_numbers import productFib, fib, fibonacci


class MyTestCase(BaseTestCase):
    def test_fib(self):
        tests = [
            self.t(0, 1),
            self.t(1, 1),
            self.t(2, 1),
            self.t(-1, 1),
            self.t(5, 120),
        ]
        for test in tests:
            self.assertEqual(test.expected, fib(test.entrance))

    def test_fibonacci(self):
        tests = [
            self.t(5, 120),
            self.t(2, 1),
            self.t(1, 1),
            # self.t(0, 1),
            # self.t(-1, 1),
        ]
        for test in tests:
            self.assertEqual(test.expected, fibonacci(test.entrance))

    def test_basics(self):
        tests = [
            self.t(productFib(4895), [55, 89, True]),
            self.t(productFib(5895), [89, 144, False]),
            self.t(productFib(0), [-1, 0, False]),
            self.t(productFib(0), [0, 1, True]),
        ]
        for test in tests:
            self.assertEqual(test.expected, fib(test.entrance))


if __name__ == '__main__':
    unittest.main()
