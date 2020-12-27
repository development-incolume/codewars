import unittest
from incolumepy.codewars.last_digit_of_a_huge_number import last_digit


class MyTestCase(unittest.TestCase):
    def test_basics(self):
        """Basic tests"""
        test_data = [
            ([], 1),
            ([0, 0], 1),
            ([0, 0, 0], 0),
        ]
        for test_input, test_output in test_data:
            print(test_input)
            self.assertEqual(last_digit(test_input), test_output)

    def test_comuns(self):
        """any more tests"""
        test_data = [
            ([1, 2], 1),
            ([3, 4, 5], 1),
            ([4, 3, 6], 4),
            ([7, 6, 21], 1),
            ([2, 2, 2, 0], 4),
        ]
        for test_input, test_output in test_data:
            print(test_input)
            self.assertEqual(last_digit(test_input), test_output)

    def test_something(self):
        """any more tests"""
        test_data = [
            ([12, 30, 21], 6),
            ([937640, 767456, 981242], 0),
            ([123232, 694022, 140249], 6),
            ([499942, 898102, 846073], 6)
        ]
        for test_input, test_output in test_data:
            print(test_input)
            self.assertEqual(last_digit(test_input), test_output)


if __name__ == '__main__':
    unittest.main()
