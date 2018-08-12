from string_questions import *
import unittest

class test_print_dups(unittest.TestCase):
    def test_empty_string(self):
        result = print_dups("")
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()

