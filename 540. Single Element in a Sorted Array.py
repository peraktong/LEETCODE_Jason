class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # binary search:
        start, stop = 0, len(nums) - 1
        while start < stop:
            mid = start + (stop - start) // 2
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] != nums[mid + 1]:
                stop = mid
            # This means there is a duplicate for mid and we skip them
            else:
                start = mid + 2

        return nums[start]



