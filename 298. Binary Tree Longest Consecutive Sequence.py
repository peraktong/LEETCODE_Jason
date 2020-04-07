# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        # DFS:
        ans = 0
        stack = [(root, 1)]
        while stack:
            node, current = stack.pop()
            if node.left:
                stack.append((node.left, current + 1 if node.left.val == node.val + 1 else 1))
            if node.right:
                stack.append((node.right, current + 1 if node.right.val == node.val + 1 else 1))

            ans = max(ans, current)

        return ans







