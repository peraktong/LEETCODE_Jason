class Solution:
    def numDecodings(self, s: str) -> int:
        ## I want to use DP
        dp = [0] * len(s)
        if s[0] == "0":
            return 0
        else:
            dp[0] = 1

        for i in range(1, len(s)):
            if 10 * int(s[i - 1]) + int(s[i]) > 26:
                dp[i] = dp[i - 1]
            elif int(s[i]) > 0:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]

        return dp[-1]


