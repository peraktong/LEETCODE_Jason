"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.step=0
        def dfs(node):
            if not node: return 0
            L,R = dfs(node.left),dfs(node.right)
            self.step +=abs(L)+abs(R)
            return node.val+L+R-1
        dfs(root)
        return self.step
"""