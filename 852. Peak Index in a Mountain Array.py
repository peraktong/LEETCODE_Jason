class Solution(object):
    def peakIndexInMountainArray(self, A):
        for i in range(len(A)):
            if A[i] > A[i + 1]:
                return i

model =Solution()
Solution.peakIndexInMountainArray()