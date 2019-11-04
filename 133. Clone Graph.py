"""


memo = {}


def clone(node):
    if node not in memo:
        c = memo[node] = Node(node.val, [])
        c.neighbors = list(map(clone, node.neighbors))
    return memo[node]


return node and clone(node)

"""