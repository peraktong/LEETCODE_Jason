class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i, num in enumerate(nums):
            if target - num in ans:
                return [ans[target - num], i]
            # save the location of each element
            ans[num] = i
