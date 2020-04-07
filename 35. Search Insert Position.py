class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = 0
        temp = nums[0]
        while target > temp and ans < len(nums) - 1:
            ans += 1
            temp = nums[ans]
        if target > temp:
            ans += 1
        return ans
