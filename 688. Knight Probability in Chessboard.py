class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        steps = ((2, 1), (2, -1), (-2, 1), (-2, -1),
                 (1, 2), (1, -2), (-1, 2), (-1, -2))
        dp = [[0] * N for i in range(N)]
        # Let dp store the probability of being on r,c at time t
        dp[r][c] = 1
        for k in range(K):
            dp2 = [[0] * N for i in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in steps:
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r + dr][c + dc] += val / 8.0
            dp = dp2
        return sum([sum(x) for x in dp])




