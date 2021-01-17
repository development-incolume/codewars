import unittest
from  incolumepy.codewars.kyu5_rot13 import rot13


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(rot13("EBG13 rknzcyr."), "ROT13 example.")
        self.assertEqual(
            rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\n"
                               "gur rkgebireg ybbxf ng gur BGURE thl'f fubrf."),
            "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\n"
            "the extrovert looks at the OTHER guy's shoes.")
        self.assertEqual(rot13("123"), "123")
        self.assertEqual(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"),
                         "This is actually the first kata I ever made. Thanks for finishing it! :)")
        self.assertEqual(rot13("@[`{"), "@[`{")


if __name__ == '__main__':
    unittest.main()
