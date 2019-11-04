class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Why don't try two scan:
        left = []
        temp = 1
        for i in nums:
            temp *= i
            left.append(temp)
        right = []
        temp = 1
        for i in reversed(nums):
            temp *= i
            right.append(temp)
        right = list(reversed(right))
        ans = [right[1]]
        for i in range(1, len(nums) - 1):
            ans.append(left[i - 1] * right[i + 1])
        ans.append(left[-2])
        return ans

