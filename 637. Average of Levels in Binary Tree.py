# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # DFS
        data = []

        def helper(node, depth=0):
            if node:
                if len(data) <= depth:
                    data.append([0, 0])
                data[depth][0] += node.val
                data[depth][1] += 1
                helper(node.left, depth + 1)
                helper(node.right, depth + 1)

        helper(root)
        return [s / float(c) for s, c in data]
