import collections

## remember use this to add 2d..
seen = collections.defaultdict(
                  lambda: collections.defaultdict(list))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # This is similar to the DFS one:
        # use a stack to store the location xy for each node

        seen = collections.defaultdict(lambda: collections.defaultdict(list))

        # x: transveral, y: depth
        def dfs(node, x=0, y=0):
            if node:
                seen[x][y].append(node)
                dfs(node.left, x - 1, y + 1)
                dfs(node.right, x + 1, y + 1)

        dfs(root)
        ans = []
        for x in sorted(seen):
            report = []
            for y in sorted(seen[x]):
                report.extend(sorted(node.val for node in seen[x][y]))
            ans.append(report)
        return ans

