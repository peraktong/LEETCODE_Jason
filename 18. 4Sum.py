class Solution(object):
    def fourSum(self, nums, target):
        # implement a fast 2-pointer to solve 2-sum
        nums.sort()
        results = []
        self.helper(nums, target, 4, [], results)
        return results

    def helper(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:
            return

        if N == 2:
            l = 0
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums) - N + 1):  # careful about range
                if target < nums[i] * N or target > nums[-1] * N:
                    break
                if i == 0 or i > 0 and nums[i - 1] != nums[i]:  # recursively reduce N
                    self.helper(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        return




