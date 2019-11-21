import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # find two sum first? O(N^2)
        temp = collections.Counter(a + b for a in A for b in B)
        return sum(temp[-c - d] for c in C for d in D)

