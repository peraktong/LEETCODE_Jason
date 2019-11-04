class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        if not root:
            return None
        stack = [root]
        # First, last are the root where the loop closes
        first, current, last = None, root.left, None
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
                continue
            if stack:
                current = stack.pop()
                if not first:
                    first = current
                if last:
                    last.right = current
                    current.left = last
                last = current
                current = current.right
        # close the loop
        first.left = last
        last.right = first
        return first