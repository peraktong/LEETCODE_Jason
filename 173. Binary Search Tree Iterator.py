# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import PriorityQueue


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.q = PriorityQueue()

        def put_p(node):
            if not node:
                return None
            self.q.put(node.val)
            put_p(node.left)
            put_p(node.right)

        put_p(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # Let's use Priority Q:
        return self.q.get()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.q.qsize() > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()