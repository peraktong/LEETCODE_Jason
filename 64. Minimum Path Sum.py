class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # DP+in place
        m = len(grid)
        n = len(grid[0])

        # initialize
        for i in range(1, m):
            grid[i][0] = grid[i - 1][0] + grid[i][0]

        for i in range(1, n):
            grid[0][i] = grid[0][i - 1] + grid[0][i]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


