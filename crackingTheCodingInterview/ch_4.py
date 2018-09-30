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
