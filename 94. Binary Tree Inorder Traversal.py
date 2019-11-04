# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # trivial recursive:

        def return_val(root, ans):
            if root != None:
                if root.left != None:
                    return_val(root.left, ans)
                ans.append(root.val)

                if root.right != None:
                    return_val(root.right, ans)

        ans = []
        return_val(root, ans)
        return ans


# iteratively:
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                # This means go go through the tree
                return res
            node = stack.pop()
            res.append(node.val)
            # If we go through all nodes, there is no root.right at the end
            root = node.right




