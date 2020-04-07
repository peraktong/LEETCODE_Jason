"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.ans = 1
        if not root:
            return 0

        def helper(node, level):
            if not node:
                return
            self.ans = max(self.ans, level)
            for c in node.children:
                helper(c, level + 1)

        helper(root, 1)
        return self.ans
