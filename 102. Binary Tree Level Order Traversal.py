# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # recursive, inorder:
        ans = []
        if not root:
            return ans

        def helper(node, level):
            # start at level 0
            if len(ans) == level:
                ans.append([])
            ans[level].append(node.val)
            # child node:
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return ans

