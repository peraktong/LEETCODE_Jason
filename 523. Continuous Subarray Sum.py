class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Let's try two pointer?:
        # non-negative
        if len(nums) < 2:
            return False

        temp = {0: -1}
        ans = 0
        for i in range(len(nums)):
            if k != 0:
                ans = (ans + nums[i]) % k
            else:
                ans += nums[i]
            if ans not in temp:
                temp[ans] = i
            elif i - temp[ans] >= 2:
                return True
        return False


