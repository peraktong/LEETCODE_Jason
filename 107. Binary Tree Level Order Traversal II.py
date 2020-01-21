# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # DFS + stack
        # stack store level and root
        stack = [(root, 0)]
        ans = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(ans) < level + 1:
                    ans.insert(0, [])
                ans[-(level + 1)].append(node.val)
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return ans


