

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isBalanced(self, root):
        return self.helper(root)[0]

    # return bool+height
    def helper(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # bottom up:
        if not root:
            return True, -1
        # check sub tree:
        l, l_h = self.helper(root.left)
        if not l:
            return False, 0
        r, r_h = self.helper(root.right)
        if not r:
            return False, 0
        # if the sub trees are balanced, check the current tree is balanced or not:
        return (abs(l_h - r_h) < 2), 1 + max(l_h, r_h)




"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def height(self, root):
        # An empty tree has height -1
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):

        # An empty tree satisfies the definition of a balanced tree
        if not root:
            return True

        # Check if subtrees have height within 1. If they do, check if the
        # subtrees are balanced
        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(
            root.left) and self.isBalanced(root.right)


"""

