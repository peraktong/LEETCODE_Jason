# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        # DFS find all parents
        def dfs(node, parent=None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        # use queue and deque the tree:
        # distance at node target is 0
        # similar to the left to right problem
        queue = collections.deque([(target, 0)])
        # start the queue from target node
        # seen is a set
        seen = set([target])
        while queue:
            # queue: key(tree node)+value
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for n in (node.left, node.right, node.parent):
                # distance +1
                if n and n not in seen:
                    seen.add(n)
                    queue.append((n, d + 1))
        # if not found
        return []






