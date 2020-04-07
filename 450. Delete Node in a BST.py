# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:  # if root doesn't exist, just return it
            return root
        # find the value based on value
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # if we find the key: delete it:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            # if we have both left and right: need a temp to store the node:
            temp = root.right
            # remove the mini in the right tree
            mini = temp.val
            while temp.left:
                temp = temp.left
                mini = temp.val
            root.val = mini
            root.right = self.deleteNode(root.right, root.val)
        return root



