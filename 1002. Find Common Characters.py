import collections
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        ans = collections.Counter(A[0])
        for i in A:
            ans = ans&collections.Counter(i)
        return list(ans.elements())