"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # use stack:
        if not head:
            return
        ans = []
        stack = [head]
        prev = Node(0)
        while stack:
            root = stack.pop()
            root.prev = prev
            prev.next = root
            prev = root
            if root.next:
                stack.append(root.next)
            if root.child:
                stack.append(root.child)
                # remove after append
                root.child = None

        head.prev = None
        return head



