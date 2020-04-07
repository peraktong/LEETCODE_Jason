class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return
        n = len(nums)
        for i in range(1, n, 2):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            if i + 1 < n and nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


