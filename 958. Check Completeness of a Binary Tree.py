# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # ? Do edge check?
        if not root:
            return False

        # Why BFS: since the BFS is parallel for each node. Use queue
        # Remember the depth of each node
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, num = nodes[i]
            i += 1
            if node:
                # remember the left node is before the right node:
                nodes.append((node.left, 2 * num))
                nodes.append((node.right, 2 * num + 1))
        # return the total numbers of the nodes: If the last one is not equal to the length of the node, this means there must be empty between nodes
        return nodes[-1][1] == len(nodes)



