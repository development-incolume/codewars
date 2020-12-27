import unittest
from incolumepy.codewars.Product_of_consecutive_Fib_numbers import productFib, fib


class MyTestCase(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(0), 1)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)

    def test_basics(self):
        self.assertEqual(productFib(4895), [55, 89, True])
        self.assertEqual(productFib(5895), [89, 144, False])
        self.assertEqual(productFib(0), [-1, 0, False])
        self.assertEqual(productFib(0), [0, 1, True])


if __name__ == '__main__':
    unittest.main()
