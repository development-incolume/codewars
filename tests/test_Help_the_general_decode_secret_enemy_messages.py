import unittest
from incolumepy.codewars.Help_the_general_decode_secret_enemy_messages import decode, encode


class MyTestCase(unittest.TestCase):
    def test_encode_decode(self):
        """ Should be compatible with encoder """
        self.assertEqual(decode(encode("Hello World!")), "Hello World!")

    def test_decode(self):
        """ Should crack encoded message """
        self.assertEqual(decode("atC5kcOuKAr!"), "Hello World!")


if __name__ == '__main__':
    unittest.main()
