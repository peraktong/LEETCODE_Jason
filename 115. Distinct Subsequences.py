class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # O(m*n)
        m = len(s) + 1
        n = len(t) + 1
        dp = [[1] * n for i in range(m)]
        for j in range(1, n):
            dp[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * (s[i - 1] == t[j - 1])
        return dp[-1][-1]


