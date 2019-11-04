# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Do BFS: have a stack to store the max sum for each node
        # Here the max sum for each node means the max sum (through only one child!)
        # Since it contains at least one node, we can do for each node:
        self.ans = float("-inf")

        def helper(node):
            # return the max sum for each node
            if not node:
                return 0
            temp = node.val
            eva = temp
            self.ans = max(self.ans, temp)
            l = helper(node.left)
            r = helper(node.right)
            if r > 0:
                temp += r
                self.ans = max(self.ans, temp)
            if l > 0:
                temp += l
                self.ans = max(self.ans, temp)
            eva += max(0, r, l)
            return eva

        helper(root)

        return self.ans
