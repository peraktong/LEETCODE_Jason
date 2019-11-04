class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # DP:
        if not nums:
            return 0
        # since we can assign + and - for each num, there will be 2 possibilities
        # Here we use stack to store the possible combination at each values
        stack = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            temp = {}
            for s in stack:
                temp[s + nums[i]] = temp.get(s + nums[i], 0) + stack.get(s, 0)
                temp[s - nums[i]] = temp.get(s - nums[i], 0) + stack.get(s, 0)
            stack = temp
        return stack.get(S, 0)



