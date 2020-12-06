import unittest
from incolumepy.codewars.decode_the_morese_code_for_real import decodeMorse, decodeBitsAdvanced


class MyTestCase(unittest.TestCase):
    def test_something(self):
        """Example from description"""
        self.assertEqual(
            decodeMorse(
                decodeBitsAdvanced(
                    '0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111'
                    '000000101100011111100000111110011101100000100000')),
            'HEY JUDE')

    def test_some_ones(self):
        """Your own tests"""
        self.assertEqual(
            decodeBitsAdvanced(
                '00000000110110100111000001100000011111101001111100111111000000000001110111111110111110111110000001'
                '01100011111100000111110011101100000100000'),
            '···· · −·−−   ·−−− ··− −·· ·')

    def test_more_ones(self):
        self.assertEqual(decodeMorse('···· · −·−−   ·−−− ··− −·· ·'), 'HEY JUDE')


if __name__ == '__main__':
    unittest.main()
