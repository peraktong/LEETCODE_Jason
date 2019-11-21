class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # O (N*n)
        n = len(needle)
        N = len(haystack)
        for i in range(N - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1



