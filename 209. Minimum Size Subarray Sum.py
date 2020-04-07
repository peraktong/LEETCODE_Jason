class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # sliding window
        # start at i
        i, res = 0, len(nums) + 1
        for j in range(len(nums)):
            s -= nums[j]
            # this means until j we have a bigger value than s: we search in this range:
            while s <= 0:
                res = min(res, j - i + 1)
                s += nums[i]
                i += 1
        return res % (len(nums) + 1)