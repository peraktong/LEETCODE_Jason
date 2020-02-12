class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # use DP to construct
        # three pointer: pay attention to 6 which is
        if n <= 0:
            return False
        if n == 1:
            return 1
        dp = [1] * n
        t2 = 0
        t3 = 0
        t5 = 0
        for i in range(1, n):
            dp[i] = min(dp[t2] * 2, dp[t3] * 3, dp[t5] * 5)
            if dp[i] == dp[t2] * 2:
                t2 += 1
            if dp[i] == dp[t3] * 3:
                t3 += 1
            if dp[i] == dp[t5] * 5:
                t5 += 1
        return dp[n - 1]
