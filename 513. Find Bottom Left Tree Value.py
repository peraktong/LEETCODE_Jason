# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS + queue
        if not root:
            return None
        queue = [root]
        for node in queue:
            if node.right:
                queue += [node.right]
            if node.left:
                queue += [node.left]
        return node.val



