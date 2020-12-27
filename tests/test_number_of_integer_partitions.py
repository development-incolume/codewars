import unittest
from incolumepy.codewars.number_of_integer_partitions import partitions


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(partitions(1), 1)
        self.assertEqual(partitions(5), 7)
        self.assertEqual(partitions(10), 42)
        self.assertEqual(partitions(25), 1958)


if __name__ == '__main__':
    unittest.main()
