# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node, lower=float("-inf"), upper=float("inf")):
            if node == None:
                return True
            value = node.val
            if value <= lower or value >= upper:
                return False
            if not helper(node.right, value, upper):
                return False
            if not helper(node.left, lower, value):
                return False

            return True

        return helper(root)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # iteration:
        stack=[]
        inorder=float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val<=inorder:
                return False
            inorder = root.val
            root =root.right
        return True
            
            
        
        

"""





