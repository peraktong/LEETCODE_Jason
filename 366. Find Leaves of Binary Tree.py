import collections


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans

        data = collections.defaultdict(list)

        def helper(node, data):
            if not node:
                return 0
            left = helper(node.left, data)
            right = helper(node.right, data)
            level = max(left, right) + 1
            data[level].append(node.val)
            return level

        helper(root, data)
        # print(data)
        for i in range(1, len(data) + 1):
            ans.append(data[i])
        return ans


