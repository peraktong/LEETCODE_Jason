class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # between i and j: if there num zero<=K, we continue to increase j
        # if num zero>K: we increase i

        i = 0
        for j in range(len(A)):
            K -= (1 - A[j])
            if K < 0:
                K += (1 - A[i])
                i += 1
        return j - i + 1



