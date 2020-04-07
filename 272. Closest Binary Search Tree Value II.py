import heapq


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        if not root:
            return None

        # data = heapq.heapify([])

        def helper(node):
            if not node:
                return
            naive.append(node.val)
            helper(node.left)
            helper(node.right)

        naive = []
        helper(root)
        naive.sort(key=lambda x: abs(x - target))
        return naive[:k]



