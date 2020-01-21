class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # sort the array first:
        A = sorted(A)
        i = 0
        j = len(A) - 1
        ans = float("-inf")
        while i < j:
            temp = A[i] + A[j]
            if temp < K:
                ans = max(ans, temp)
                i += 1
            else:
                j -= 1
        return ans if ans != float("-inf") else -1


