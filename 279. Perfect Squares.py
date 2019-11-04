class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # DP
        target = [i**2 for i in range(int(n**0.5)+1)]
        dp = [float("inf")]*(n+1)
        # initialize
        dp[0]=0
        for i in range(1,n+1):
            for t in target:
                if i<t:
                    # this means we can not find a square in target
                    break
                dp[i] = min(dp[i],dp[i-t]+1)
        return dp[n]