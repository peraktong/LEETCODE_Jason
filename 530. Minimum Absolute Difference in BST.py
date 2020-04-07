# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # dfs+ inorder
        temp = []

        def helper(node):
            if node.left:
                helper(node.left)
            temp.append(node.val)
            if node.right:
                helper(node.right)

        helper(root)
        ans = float("inf")
        for i in range(len(temp[:-1])):
            ans = min(ans, abs(temp[i + 1] - temp[i]))
        return ans


