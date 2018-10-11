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

    def test_path_exists(self):
        self.assertEqual(path_exists({1: []}, 1, 1), False)
        self.assertEqual(path_exists({1: [1]}, 1, 1), True)
        self.assertEqual(path_exists({1: [2]}, 1, 2), True)
        self.assertEqual(path_exists({1: [2]}, 2, 1), False)
        self.assertEqual(path_exists({1: [2], 2: []}, 1, 2), True)
        self.assertEqual(path_exists({1: [2], 2: []}, 2, 1), False)
        self.assertEqual(path_exists({1: [2], 2: [2]}, 1, 2), True)
        self.assertEqual(path_exists({1: [2], 2: [2]}, 2, 1), False)
        self.assertEqual(path_exists({1: [2], 2: [1]}, 1, 2), True)
        d = {
                1: [2],
                2: [1, 3],
                3: [1, 2, 3, 4],
                4: [1],
        }
        self.assertEqual(path_exists(d, 1, 4), True)

    def test_make_from_list(self):
        assert make_from_list("") == None
        assert make_from_list("a") == BinaryTree("a")
        assert make_from_list("12") == BinaryTree("2", BinaryTree("1"))
        assert make_from_list([1, 2]) == BinaryTree(2, BinaryTree(1))

    def test_layerize(self):
        assert layerize(None) == []
        assert layerize(make_from_list("a")) == [[BinaryTree("a")]]
        assert layerize(make_from_list("abc")) == [[BinaryTree("b", BinaryTree("a"), BinaryTree("c"))], [BinaryTree("a"),BinaryTree("c")]]
        x = [n for n in range(10)]
        expected = [
                [make_from_list(x)],
                [make_from_list(x[:5]), make_from_list(x[6:])],
                [make_from_list(x[:2]), make_from_list(x[3:5]), make_from_list(x[6:8]), make_from_list([9])],
                [make_from_list([0]), make_from_list([3]), make_from_list([6])]
        ]
        assert layerize(make_from_list(x)) == expected

    def test_make_from_array_like(self):
        tree = make_from_array_like([1, 2, 3, 4])
        expected = BinaryTreeWithParent(3)
        expected.left = BinaryTreeWithParent(2, expected)
        expected.left.left = BinaryTreeWithParent(1, expected.left)
        expected.right = BinaryTreeWithParent(4, expected)
        assert tree == expected

    def test_in_order_successor(self):
        tree = make_from_array_like([i for i in range(100)])
        for i in range(100):
            assert in_order_successor(tree.find(i)) is tree.find(i+1)
        tree = make_from_array_like("abcdefghijklmnopqrstuvwxyz")
        for i in range(26):
            assert in_order_successor(tree.find(i)) is tree.find(i+1)


if __name__ == '__main__':
    unittest.main()
