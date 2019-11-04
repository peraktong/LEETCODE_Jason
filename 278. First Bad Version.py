# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # let's to split by two:
        start = 0
        stop = n
        loc = n // 2
        while start < stop:
            if not isBadVersion(loc):
                start = loc
            else:
                stop = loc
            loc = start + (stop - start) // 2
            if stop - start == 1:
                return stop

