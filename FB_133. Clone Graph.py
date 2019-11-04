"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # always check the edge case:


        # DFS:
        stack ={}
        def helper(node):
            if node not in stack:
                temp = stack[node] = Node(node.val,[])
                temp.neighbors=list(map(helper,node.neighbors))
            return stack[node]
        return node and helper(node)
        