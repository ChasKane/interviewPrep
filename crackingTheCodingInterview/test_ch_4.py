from ch_4 import *
import unittest

class test_ch_4(unittest.TestCase):
    def test_is_balanced(self):
        self.assertEqual(is_balanced(Tree(1)), True)
        self.assertEqual(is_balanced(Tree(1, [Tree(2)])), True)
        self.assertEqual(is_balanced(Tree(1, [Tree(2, [Tree(3)])])), False)
        t1 = Tree(1)
        t2 = Tree(2)
        t3 = Tree(3)
        t4 = Tree(4, [t1, t2, t3])
        t5 = Tree(5)
        t6 = Tree(6)
        t7 = Tree(7, [t5, t6])
        t8 = Tree(8, [t4, t7])
        r = Tree(9, [t8])
        self.assertEqual(is_balanced(r), False)
        self.assertEqual(is_balanced(t8), True)

    def test_is_balanced(self):
        self.assertEqual(is_balanced(Tree(1)), True)
if __name__ == '__main__':
    unittest.main()
