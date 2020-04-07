class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        N = len(A)
        ans = 0
        current = 0
        for i in range(N):
            if i >= 2 and (A[i] > A[i - 1] < A[i - 2] or A[i] < A[i - 1] > A[i - 2]):
                current += 1
            elif i >= 1 and A[i] != A[i - 1]:
                current = 2
            else:
                current = 1
            ans = max(ans, current)
        return ans









