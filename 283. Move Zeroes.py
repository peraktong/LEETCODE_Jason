nums = [0,1,0,3,12]


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[index_zero] = nums[index_zero], nums[i]
                index_zero += 1

        print(nums)

model = Solution()
model.moveZeroes(nums=nums)
