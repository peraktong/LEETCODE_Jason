# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # recursive
        if not root:
            return None
        data = []

        def helper(node):
            if not node:
                return
            data.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        data.sort()
        ans = float("inf")
        for i in range(1, len(data)):
            ans = min(ans, abs(data[i] - data[i - 1]))
        return ans


