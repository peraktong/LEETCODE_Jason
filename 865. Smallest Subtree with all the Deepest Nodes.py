# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        ans = None
        if not root:
            return ans
        # pair child and parent:

        depth = {None: -1}

        def dfs(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        max_depth = max(depth.values())

        def helper(node):
            if not node or depth.get(node, None) == max_depth:
                return node
            L, R = helper(node.left), helper(node.right)
            return node if L and R else L or R

        return helper(root)




