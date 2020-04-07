# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        # inorder
        def in_hashset(node):
            return in_hashset(node.left) | set([target - node.val]) | in_hashset(node.right) if node else set()

        # check
        def in_check(node):
            return in_check(node.left) or (node.val in s) or in_check(node.right) if node else False

        s = in_hashset(root2)
        return in_check(root1)



