# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = {}

        def helper(node):
            if not node:
                return 0
            temp = node.val + helper(node.left) + helper(node.right)
            ans[temp] = ans.get(temp, 0) + 1
            return temp

        helper(root)
        maxi = max(ans.values())
        res = []
        for i, v in ans.items():
            if v == maxi:
                res.append(i)
        return res
