from math import e, log
import math


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        return int(math.floor(x ** 0.5))
