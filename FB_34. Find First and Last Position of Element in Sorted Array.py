class Solution:
    def extreme_insertion_index(self, nums, target, left):

        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if target < nums[mid] or (left and target == nums[mid]):
                high = mid
            else:
                low = mid + 1
        return low

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx = self.extreme_insertion_index(nums, target, True)

        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]



