"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return ans

        def helper(node):
            if not node:
                return
            ans.append(node.val)
            if node.children:
                for c in node.children:
                    helper(c)

        helper(root)
        return ans
