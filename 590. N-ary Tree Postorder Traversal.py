"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []

        def helper(node):
            if not node:
                return
            if node.children:
                for c in node.children:
                    helper(c)

            ans.append(node.val)

        helper(root)
        return ans
