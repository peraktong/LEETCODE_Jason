class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        ans = A[L + M - 1]
        Lmax, Mmax = A[L - 1], A[M - 1]
        for i in range(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - M - L])
            Mmax = max(Mmax, A[i - L] - A[i - M - L])
            ans = max(ans, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
        return ans


