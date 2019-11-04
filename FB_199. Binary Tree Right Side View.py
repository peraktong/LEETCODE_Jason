# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # DFS:
        ans = []

        def dfs(node, depth):
            if node:
                if depth == len(ans):
                    ans.append(node.val)
                dfs(node.right, depth + 1)
                dfs(node.left, depth + 1)

        dfs(root, 0)
        return ans
