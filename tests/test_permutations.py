import unittest
from incolumepy.codewars.permutations import permutations


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sorted(permutations('a')), ['a']);
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
        self.assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])


if __name__ == '__main__':
    unittest.main()
