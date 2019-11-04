class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        # DP, use dictionary to store the
        # Here the ket is index and the difference for this arithmetic array
        # the values are the length of the arithmetic array at this index:
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())





