class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        ans = nums[0] * nums[1] * nums[2]
        if len(nums) == 3:
            return ans
        nums.sort(key=lambda x: abs(x))
        a, b, c = len(nums) - 1, len(nums) - 2, len(nums) - 3
        self.ans = nums[a] * nums[b] * nums[c]

        def helper(a, b, c):

            if c < 0:
                return
            # print(self.ans,a,b,c)
            self.ans = max(self.ans, nums[a] * nums[b] * nums[c])
            # print(self.ans,a,b,c)
            if self.ans >= 0:
                return
            else:
                c -= 1
                helper(a, b, c)
                helper(a, b - 1, c)
                helper(a - 1, b - 1, c)

        helper(a, b, c)
        return self.ans



