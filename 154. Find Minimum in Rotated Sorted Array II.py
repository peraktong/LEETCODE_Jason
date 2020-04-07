class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                pass
            else:
                ans = nums[i]
                break
        return ans

