class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # You can understand them as alphabetic order:
        # backward
        i = j = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        # nums are in descending order:
        if i == 0:
            nums.reverse()
            return
            # Find the last ascending element:
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        # Let's reverse the second part of the list:
        l = k + 1
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1



