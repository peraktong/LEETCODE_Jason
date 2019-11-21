class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # cycle replacement:

        N = n = len(nums)
        k = k % N
        j = 0
        while n > 0 and k % n != 0:
            for i in range(k):
                # swap cycle
                nums[j + i], nums[N - k + i] = nums[N - k + i], nums[j + i]
            n, j = n - k, j + k
            k = k % n


