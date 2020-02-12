class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp
        if n == 0:
            return 1

        ans = 10
        unique = 9
        available = 9
        for i in range(n - 1):
            unique = unique * available
            ans += unique
            available -= 1
        return ans

