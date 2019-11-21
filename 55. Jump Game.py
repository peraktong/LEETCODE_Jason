class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        dp = [0] * len(nums)
        dp[0] = nums[0]
        # use dp to store the max distance you can travel from this index:
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] - 1, nums[i])
        return all(m != 0 for m in dp[:-1])


