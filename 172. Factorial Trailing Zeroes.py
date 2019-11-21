class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # mathematical solution on green book
        i = 1
        ans = 0
        while 5 ** i < n + 1:
            ans += n // 5 ** i
            i += 1
        return ans

