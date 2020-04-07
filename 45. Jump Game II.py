class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy:
        n = len(nums)
        if n < 2:
            return 0

        # we remember the max position each point can reach:
        max_pos = nums[0]
        max_step = nums[0]
        ans = 1
        for i in range(1, n):

            if max_step < i:
                # This means we  still need more steps to reach this point:
                ans += 1
                max_step = max_pos
            max_pos = max(max_pos, nums[i] + i)
        return ans




