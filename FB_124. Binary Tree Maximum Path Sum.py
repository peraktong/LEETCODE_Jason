# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = float("-inf")

        def helper(node):
            if not node:
                return 0
            # set these gain>0
            left_gain = max(helper(node.left), 0)
            right_gain = max(helper(node.right), 0)
            max_val = node.val + left_gain + right_gain
            self.ans = max(self.ans, max_val)
            return node.val + max(left_gain, right_gain)

        helper(root)
        return self.ans

