class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i = 0
        while s:
            ans += (ord(s[-1]) - ord("A") + 1) * (26 ** i)
            i += 1
            s = s[:-1]
        return ans
