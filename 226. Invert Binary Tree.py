"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive:
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right=left
        return root

# iteration:
stack = [root]
while stack:
    node = stack.pop()
    if node:
        ode.left, node.right = node.right, node.left
        stack += node.left, node.right
return root

"""