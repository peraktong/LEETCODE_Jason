"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # DFS:
        if not root:
            return


        stack = [root]
        while stack:
            current = stack.pop()
            if current.left and current.right:
                current.left.next = current.right
                # This means current next is pointing to another node (like 2-3)
                if current.next:
                    current.right.next = current.next.left
                stack.append(current.right)
                stack.append(current.left)
        return root

        