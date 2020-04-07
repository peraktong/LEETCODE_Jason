# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        # inorder
        if not t:
            return ""
        ans = str(t.val)
        if t.left:
            ans += "(" + self.tree2str(t.left) + ")"
        if not t.left and t.right:
            ans += "()"
        if t.right:
            ans += "(" + self.tree2str(t.right) + ")"

        return ans


