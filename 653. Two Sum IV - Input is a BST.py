# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # recursive:
        if not root:
            return False
        bfs, s = [root], set([])
        for b in bfs:
            if k - b.val in s:
                return True
            s.add(b.val)
            if b.left:
                bfs.append(b.left)
            if b.right:
                bfs.append(b.right)

        return False
