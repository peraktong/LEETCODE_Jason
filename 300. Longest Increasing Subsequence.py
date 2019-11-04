class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        # dp
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            # check all nums before i: if j<i, which means i is increasing ans we check this
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
