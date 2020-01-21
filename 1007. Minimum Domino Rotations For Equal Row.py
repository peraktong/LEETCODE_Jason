class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # it should satisfy that countA[i] + countB[i] - same[i] = n
        n = len(A)
        same = [0] * 7
        count_a = [0] * 7
        count_b = [0] * 7
        for i in range(n):
            count_a[A[i]] += 1
            count_b[B[i]] += 1
            if A[i] == B[i]:
                same[A[i]] += 1
        for i in range(1, 7):
            if count_a[i] + count_b[i] - same[i] == n:
                return n - max(count_a[i], count_b[i])
        return -1




