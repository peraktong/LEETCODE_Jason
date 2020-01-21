# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        # recursive:
        def helper(start, end):
            if start > end:
                return [None, ]
            ans = []
            for i in range(start, end + 1):
                # all possible left subtrees
                left_trees = helper(start, i - 1)
                # all possible right subtrees
                right_trees = helper(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        ans.append(current_tree)
            return ans

        return helper(1, n) if n else []


