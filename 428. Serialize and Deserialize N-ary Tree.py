from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        # inorder:
        serial = []

        def preorder(node):

            if not node:
                return

            serial.append(str(node.val))

            for child in node.children:
                preorder(child)

            serial.append("#")  # indicates no more children, continue serialization from parent

        preorder(root)
        return " ".join(serial)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        tokens = deque(data.split())
        root = Node(int(tokens.popleft()), [])

        def build(node):
            if not tokens:
                return
            while tokens[0] != "#":
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                build(child)
            # encounter "#"
            tokens.popleft()

        build(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))