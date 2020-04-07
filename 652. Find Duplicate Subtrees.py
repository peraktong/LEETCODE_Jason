import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # DFS:
        count = collections.Counter()
        ans = []
        def helper(node):
            if not node:
                return "#"
            ls = "{},{},{}".format(node.val,helper(node.left),helper(node.right))
            count[ls]+=1
            if count[ls]==2:
                ans.append(node)
            return ls
        helper(root)
        return ans