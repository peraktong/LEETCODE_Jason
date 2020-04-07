class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # sort:
        # just math
        N = int(len(nums) / 2)
        ans = 0
        nums.sort()
        for i in range(N):
            ans += nums[2 * i]
        return ans

