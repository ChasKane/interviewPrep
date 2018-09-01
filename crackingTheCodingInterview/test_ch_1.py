from ch_1 import *
import unittest

class test_ch_1(unittest.TestCase):
    def test_unique_characters(self):
        self.assertEqual(unique_characters("aa"), False)
        self.assertEqual(unique_characters("aaaaaaaaaaaaaaaaaa"), False)
        self.assertEqual(unique_characters("abcade"), False)

        self.assertEqual(unique_characters("a"), True)
        self.assertEqual(unique_characters("abcde"), True)
        self.assertEqual(unique_characters("edcb"), True)

    def test_c_reverse(self):
        self.assertEqual(c_reverse("a "), "a ")
        self.assertEqual(c_reverse("aa "), "aa ")
        self.assertEqual(c_reverse("ab "), "ba ")
        self.assertEqual(c_reverse("cba "), "abc ")
        self.assertEqual(c_reverse("yzxa "), "axzy ")

if __name__ == '__main__':
    unittest.main()
