import queue
class Tree():
    def __init__(self, data=None, children=[]):
        self.data = data
        self.children = children
    def height(self):
        if not self.children: return 0
        heights = []
        for t in self.children:
            heights.append(t.height())
        return 1 + max(heights)
    def min_height(self):
        if not self.children: return 0
        heights = []
        for t in self.children:
            heights.append(t.min_height())
        return 1 + min(heights)

class BinaryTree():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return getSortedList(self) == getSortedList(other)

class BinaryTreeWithParent():
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        return getSortedList(self) == getSortedList(other)

    def find(self, n):
        if self.data == n:
            return self
        if self.left and self.data > n:
            return self.left.find(n)
        if self.right and self.data < n:
            return self.right.find(n)
        return None

# Helper function in lue of a better way to do this (see
# http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html
# for said better way)
def getSortedList(node):
    if not node: return []
    l = getSortedList(node.left)
    r = getSortedList(node.right)
    return l + [node.data] + r

def make_from_array_like(arr, parent=None):
    if not arr: return
    n = len(arr)
    mid = int(n/2)

    if n == 1:
        return BinaryTreeWithParent(arr[0], parent)

    v = BinaryTreeWithParent(arr[mid], parent)
    v.left = make_from_array_like(arr[:mid], v)
    v.right = make_from_array_like(arr[mid+1:], v)
    return v

# 4.1
# Implement a function to check if a tree is balanced. For the purposes of this
# question, a balanced tree is defined to be a tree such that no two leaf nodes differ
# in distance from the root by more than one
# INPUT: root node of a tree
# OUTPUT: True or False
def is_balanced(r):
    if not r.children: return True
    heights = []
    for t in r.children:
        heights.append(t.height())
    if len(heights) == 1 and heights[0] > 0:
        return False
    return max(heights) - min(heights) < 2

# 4.2
# Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes.
# INPUT: edge list represented as a python dictionary
# OUTPUT: True or False
def path_exists(d, a, b):
    q = queue.Queue()
    q.put(a)
    seen = set()
    while not q.empty():
        x = q.get()
        if x in seen:
            continue
        seen.add(x)
        y = d.get(x, [])
        for v in y:
            if b == v: return True
            q.put(v)
    return False

# 4.3
# Given a sorted (increasing order) array, write an algorithm to create a
# binary tree with minimal height.
# INPUT: sorted list of numbers
# OUTPUT: BinaryTree node that is the root of a min-height binary (search) tree representing the input array
def make_from_list(s):
    if not s: return None
    if len(s) == 1: return BinaryTree(s[0])
    return BinaryTree(
            s[int(len(s)/2)],
            make_from_list(s[:int(len(s)/2)]),
            make_from_list(s[int(len(s)/2) + 1:])
        )

# 4.4
# Given a binary search tree, design an algorithm which creates a linked list
# of all the nodes at each depth (eg, if you have a tree with depth D, you’ll have D linked lists)
# INPUT: a well formed BST
# OUTPUT: a list of linked lists, each member of which is a node in the original tree as described
def layerize(T):
    if not T: return []
    ret = [[T]]
    current_layer = [T]
    while current_layer:
        next_layer = []
        for v in current_layer:
            if v.left: next_layer.append(v.left)
            if v.right: next_layer.append(v.right)
        if next_layer:
            ret.append(next_layer)
        current_layer = next_layer
    return ret

# 4.5
# Write an algorithm to find the ‘next’ node (e g , in-order successor) of a given node in a
# binary search tree where each node has a link to its parent
# INPUT: a node in a BST composed of nodes with links to their parents and children.
# OUTPUT: the in-order successor of the input node in the same tree.
def in_order_successor(n):
    if not n: return None
    if not n.right:
        while n.parent:
            if n.parent.right is n:
                n = n.parent
            else:
                n = n.parent
                break
        else:
            return None
    else:
        n = n.right
        while n.left:
            n = n.left
    return n
