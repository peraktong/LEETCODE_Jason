class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # DFS:

        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        # Here we store index for s1 s2 in stack
        stack = [(0, 0)]
        visited = set((0, 0))
        while stack:
            m, n = stack.pop()
            if m + n == l:
                return True
            if m + 1 <= r and s1[m] == s3[m + n] and (m + 1, n) not in visited:
                stack.append((m + 1, n))
                visited.add((m + 1, n))
            if n + 1 <= c and s2[n] == s3[m + n] and (m, n + 1) not in visited:
                stack.append((m, n + 1))
                visited.add((m, n + 1))
        return False


