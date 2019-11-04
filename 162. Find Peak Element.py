class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary search:

        start, stop = 0, len(nums) - 1
        while start < stop:
            mid = start + (stop - start) // 2
            if nums[mid] > nums[mid + 1]:
                stop = mid
            else:
                start = mid + 1
        # index
        return start
