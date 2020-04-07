# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.temp = {}

        def helper(node, level):
            if not node:
                return
            self.temp[level] = max(self.temp.get(level, float('-inf')), node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        helper(root, 0)
        ans = []
        for x, v in self.temp.items():
            ans.append(v)
        return ans


