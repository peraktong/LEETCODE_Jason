# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                # search right first:
                # Then this view will increas and left won;t inlfuence the results
                collect(node.right, depth + 1)
                collect(node.left, depth + 1)

        view = []
        collect(root, 0)
        return view
