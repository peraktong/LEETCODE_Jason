# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.tot = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # flatten the tree first?
        if root is not None:
            self.convertBST(root.right)
            self.tot += root.val
            root.val = self.tot
            self.convertBST(root.left)
        return root

