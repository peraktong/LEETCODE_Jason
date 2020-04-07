# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = []

        # Here path is a str
        def helper(node, path):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                self.ans.append(path)
                return
            helper(node.left, path)
            helper(node.right, path)

        helper(root, "")
        print(self.ans)
        return sum([int(t) for t in self.ans])

