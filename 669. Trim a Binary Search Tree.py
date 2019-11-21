# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # recursive:
        def helper(node):
            if not node:
                return None
            elif node.val>R:
                # trim right+node keep left
                return helper(node.left)
            elif node.val<L:
                return helper(node.right)
            else:
                # between: trim part of the left/right branch
                node.left = helper(node.left)
                node.right = helper(node.right)
                return node
        return helper(root)