# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self.ans += abs(left - right)
            return left + right + node.val

        self.ans = 0
        helper(root)
        return self.ans

