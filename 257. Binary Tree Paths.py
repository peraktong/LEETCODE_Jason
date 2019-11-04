# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.ans = []

        # recursive:
        def helper(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    self.ans.append(path)
                else:
                    path += "->"
                    helper(root.left, path)
                    helper(root.right, path)

        helper(root, "")
        return self.ans




