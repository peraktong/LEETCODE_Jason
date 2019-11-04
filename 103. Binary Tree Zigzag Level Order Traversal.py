# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq


class Solution(object):
    def zigzagLevelOrder(self, root):

        # BFS:
        if not root:
            return []
        ans = []
        temp = []
        stack = [root]
        flag = 1
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                temp += [node.val]
                if node.left:
                    stack += [node.left]
                if node.right:
                    stack += [node.right]
            # Here flag=1 or -1, and ::
            if flag == 1:
                ans += [temp]
            else:
                ans += [temp[::-1]]
            temp = []
            flag *= -1

        return ans





