# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []

        def helper(node):
            if not node:
                return
            ans.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        return ans
