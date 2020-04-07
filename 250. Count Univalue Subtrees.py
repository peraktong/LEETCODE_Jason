# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        if not root:
            return self.ans
        self.helper(root)
        return self.ans
        # DFS:

    def helper(self, node):
        if node.left is None and node.right is None:
            self.ans += 1
            return True
        is_uni = True
        if node.left:
            is_uni = self.helper(node.left) and is_uni and node.left.val == node.val
        if node.right:
            is_uni = self.helper(node.right) and is_uni and node.right.val == node.val
        if is_uni:
            self.ans += 1
        return is_uni


