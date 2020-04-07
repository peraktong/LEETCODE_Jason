class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        # find the pivot point + binary searching:
        i = len(nums) - 1
        while i > 0:
            if nums[i] < nums[i - 1]:
                ans = nums[i]
            i -= 1
        return ans



