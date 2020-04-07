import collections


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []

        def preorder(node):
            if node:
                data.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return " ".join(map(str, data))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = collections.deque([int(val) for val in data.split()])

        def build(min_val, max_val):
            if values and min_val < values[0] < max_val:
                value = values.popleft()
                node = TreeNode(value)
                node.left = build(min_val, value)
                node.right = build(value, max_val)
                return node

        return build(float("-inf"), float("inf"))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))