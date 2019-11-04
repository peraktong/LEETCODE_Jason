class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # one way:
        ans = temp = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp += 1
            else:
                ans = max(ans, temp)
                temp = 1
        ans = max(ans, temp)
        return ans

