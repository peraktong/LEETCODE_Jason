# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # dfs
        if not root:
            return root
        data = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            data.append(node.val)
            dfs(node.right)

        dfs(root)
        ans = cur = TreeNode(None)
        for c in data:
            cur.right = TreeNode(c)
            cur = cur.right
        return ans.right


