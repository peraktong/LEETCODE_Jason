
root = 1
import collections
def solutions(node):
    cols = collections.defaultdict(list)
    queue = collections.deque([root,0])

    while queue:
        node,i = queue.popleft()
        if node:
            cols[i].append(node.val)
            queue+=(node.left,i-1),(node.right,i+1)
    return [cols[i] for i in sorted(cols)]