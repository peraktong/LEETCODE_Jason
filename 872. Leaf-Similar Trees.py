# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        # DFS
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                yield node.val
            for i in dfs(node.left):
                yield i
            for i in dfs(node.right):
                yield i

        return list(dfs(root1)) == list(dfs(root2))

