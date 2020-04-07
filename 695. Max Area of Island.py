class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS:
        if not grid:
            return 0
        seen = set()

        def helper(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + helper(r - 1, c) + helper(r + 1, c) + helper(r, c - 1) + helper(r, c + 1))

        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans = max(ans, helper(r, c))
        return ans
