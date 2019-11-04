# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Here (a,b): a is the max value that you can rob with root= this node
    # b is similar to a but without rob the node
    def rob(self, root):
        return self.dfs(root)[1];

    def dfs(self, node):
        if not node:
            return (0, 0)
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        f2 = l[1] + r[1]
        f1 = l[0] + r[0]
        return (f2, max(f2, f1 + node.val))


