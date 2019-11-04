class Solution:
    def rob(self, nums: List[int]) -> int:
        # Dynamic programming:
        previous_max = 0
        current_max = 0
        for i in nums:
            # This means each time we check the current max, and if it's bigger, add
            # i to previous max
            temp = current_max
            current_max = max(current_max, previous_max + i)
            previous_max = temp

        return current_max
