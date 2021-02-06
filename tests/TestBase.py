import unittest
from collections import namedtuple


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.t = namedtuple('test', 'entrance expected')


if __name__ == '__main__':
    unittest.main()
