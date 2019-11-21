# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """

        """
        The inorder traversal of a BST is the nodes in ascending order. 
        To find a successor, you just need to find the smallest one that 
        is larger than the given value since there are no duplicate values
         in a BST. It just like the binary search in a sorted list.
        
        """
        ans = None
        while root:
            if p.val < root.val:
                ans = root
                # looking for smaller
                root = root.left
            else:
                root = root.right
        return ans



