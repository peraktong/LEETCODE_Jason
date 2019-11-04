class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sys.maxsize
        profile = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif (prices[i] - buy > profile):
                profile = prices[i] - buy
        return profile

