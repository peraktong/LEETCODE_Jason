class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp:
        if len(prices) < 2:
            return 0
        sell, buy, sell_prev, buy_prev = 0, -prices[0], 0, 0
        for price in prices:
            buy_prev = buy
            buy = max(sell_prev - price, buy_prev)
            sell_prev = sell
            sell = max(buy_prev + price, sell_prev)
        return sell


