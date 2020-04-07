# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # recursive

        def helper(node):
            if not node:
                return
            if node.left:
                if not node.left.left and not node.left.right:
                    self.ans += node.left.val
                helper(node.left)
            if node.right:
                helper(node.right)

        self.ans = 0
        helper(root)
        return self.ans


