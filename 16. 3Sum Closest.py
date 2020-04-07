class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == target:
                    return temp
                if abs(temp - target) < abs(ans - target):
                    ans = temp
                if temp < target:
                    j += 1
                if temp > target:
                    k -= 1
        return ans


