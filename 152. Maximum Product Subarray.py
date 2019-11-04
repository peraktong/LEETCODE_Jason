class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # since it's integer, it's easier since the abs value is always increasing unless we have 0:
        # split the array with negative values:
        A = nums
        B = A[::-1]
        for i in range(1, len(A)):
            # If 0, use 1
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)


