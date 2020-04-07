# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return None
        temp = {}

        def helper(node, level, trans):
            if not node:
                return
            if level in temp:
                temp[level].append(trans)
            else:
                temp[level] = []
                temp[level].append(trans)
            # left:
            if node.left:
                helper(node.left, level + 1, trans * 2)
            if node.right:
                helper(node.right, level + 1, trans * 2 + 1)

        helper(root, 0, 0)
        # print(temp)
        ans = [max(x) - min(x) + 1 for x in temp.values()]
        return max(ans)


