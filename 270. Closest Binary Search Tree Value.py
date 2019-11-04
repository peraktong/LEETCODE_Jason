# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # binary search

        closest = root.val
        while root:
            closest = min(closest, root.val, key=lambda x: abs(x - target))
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closest




