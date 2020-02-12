class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        # we can break them into numbers<4, which leads to the biggest value
        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        ans *= n
        return ans


