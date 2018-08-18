from string_questions import *
import unittest

class test_print_dups(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(print_dups(""), "")
    def test_a_few_strings(self):
        self.assertEqual(print_dups("aa"), "a")
        self.assertEqual(print_dups("abcdefghijklmnop"), "")
        self.assertEqual(print_dups("abcdefghijklmnopaa"), "aa")

if __name__ == '__main__':
    unittest.main()

