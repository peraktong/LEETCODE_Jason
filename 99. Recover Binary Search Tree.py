# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # sort an almost array where two elements are swapped

        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        def find_swap(nums):
            N = len(nums)
            x = y = None
            for i in range(N - 1):
                if nums[i] > nums[i + 1]:
                    # first swap
                    y = nums[i + 1]
                    if x == None:
                        # second swap
                        x = nums[i]
                    else:
                        # This means we find the second swap x
                        break
            return x, y

        def recover(node, count):
            # do inorder:
            if node:
                if node.val == x or node.val == y:
                    # swap
                    node.val = y if node.val == x else x
                    count -= 1
                    if count == 0:
                        return
                recover(node.left, count)
                recover(node.right, count)

        nums = inorder(root)
        x, y = find_swap(nums)
        # Find 2 swaps
        recover(root, 2)






