from string_questions import *
import unittest

class test_print_dups(unittest.TestCase):
    def test_a_few_strings(self):
        self.assertEqual(print_dups("aa"), "a")
        self.assertEqual(print_dups("abcdefghijklmnop"), "")
        self.assertEqual(print_dups("abcdefghijklmnopaa"), "aa")
class test_is_anagram(unittest.TestCase):
    def test_a_few_strings(self):
        self.assertEqual(is_anagram("aa", ""), False)
        self.assertEqual(is_anagram("abcd", "badc"), True)
class test_first_nonrepeated_character(unittest.TestCase):
    def test_a_few_strings(self):
        self.assertEqual(first_nonrepeated_character("aa"), "")
        self.assertEqual(first_nonrepeated_character("aabcdefghijklmnopbd"), "c")
        self.assertEqual(first_nonrepeated_character("abcdabcdabcd"), "")

if __name__ == '__main__':
    unittest.main()
