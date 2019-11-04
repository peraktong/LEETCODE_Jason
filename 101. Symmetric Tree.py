# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def ismirror(self, t1, t2):
        if t1 == None and t2 == None:
            return True

        if t1 == None or t2 == None:
            return False

        if t1.val == t2.val:
            inner = self.ismirror(t1.left, t2.right)
            outter = self.ismirror(t1.right, t2.left)
            return inner and outter
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        # recursive:
        if root == None:
            return True
        else:
            return self.ismirror(root.left, root.right)

