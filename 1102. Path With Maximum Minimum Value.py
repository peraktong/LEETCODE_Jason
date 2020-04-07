import heapq


class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        # use Heap:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(A)
        n = len(A[0])
        heap = [(-A[0][0], 0, 0)]
        visited = [[0] * n for i in range(m)]
        # use heap from small to big, which means pop the big first(big means smallest min)
        while heap:
            val, x, y = heapq.heappop(heap)
            if x == m - 1 and y == n - 1:
                return -val
            for d in directions:
                dx = x + d[0]
                dy = y + d[1]
                if dx >= 0 and dx < m and dy >= 0 and dy < n and not visited[dx][dy]:
                    visited[dx][dy] = 1
                    heapq.heappush(heap, (max(val, -A[dx][dy]), dx, dy))
        return -1







