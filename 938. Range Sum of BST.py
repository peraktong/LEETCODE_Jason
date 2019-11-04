"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        def search(node):
            if node:
                if L<=node.val<=R:
                    self.value+=node.val
                if node.val>L:
                    search(node.left)

                if node.val<R:
                    search(node.right)

        self.value=0
        search(root)

        return self.value

"""