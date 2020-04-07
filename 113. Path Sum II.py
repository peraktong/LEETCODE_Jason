# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        stack = [(root, sum - root.val, [root.val])]
        while stack:
            cur, val, array = stack.pop()
            if not cur.left and not cur.right and val == 0:
                ans.append(array)
            if cur.right:
                stack.append((cur.right, val - cur.right.val, array + [cur.right.val]))
            if cur.left:
                stack.append((cur.left, val - cur.left.val, array + [cur.left.val]))
        return ans

