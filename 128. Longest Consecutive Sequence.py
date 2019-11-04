class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) means we can not sort the list:
        # Also we can not use heap

        ans = 0
        num_set = set(nums)

        for num in num_set:
            # we only find ascending order ones
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                ans = max(ans, current_streak)
        return ans

