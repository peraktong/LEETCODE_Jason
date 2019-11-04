coins = [1, 2, 5]
amount = 11


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## DP:

        # If amount=0, no need
        dp = [0] + [float("inf")] * amount
        for coin in coins:
            # If there is such coin, the amount must be bigger than this coin
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1

