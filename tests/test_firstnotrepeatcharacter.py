import unittest
from incolumepy.codewars.firstnotrepeatcharacter import first_non_repeating_letter


class MyTestCase(unittest.TestCase):
    def test_1(self):
        """should handle simple tests"""
        self.assertEqual(first_non_repeating_letter('a'), 'a')
        self.assertEqual(first_non_repeating_letter('stress'), 't')
        self.assertEqual(first_non_repeating_letter('moonmen'), 'e')

    def test_2(self):
        """should handle empty strings"""
        self.assertEqual(first_non_repeating_letter(''), '')

    def test_3(self):
        """should handle all repeating strings"""
        self.assertEqual(first_non_repeating_letter('abba'), '')
        self.assertEqual(first_non_repeating_letter('aa'), '')

    def test_4(self):
        """should handle odd characters"""
        self.assertEqual(first_non_repeating_letter('~><#~><'), '#')
        self.assertEqual(first_non_repeating_letter('hello world, eh?'), 'w')

    def test_5(self):
        """should handle letter cases"""
        self.assertEqual(first_non_repeating_letter('sTreSS'), 'T')
        self.assertEqual(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')


if __name__ == '__main__':
    unittest.main()
