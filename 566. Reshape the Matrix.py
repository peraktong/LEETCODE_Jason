class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        tot = len(nums) * len(nums[0])
        # sanity check:
        if tot < r * c:
            return nums
        ans = [[0] * c for i in range(r)]
        cr = 0
        cc = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if cc >= c:
                    cc = 0
                    cr += 1
                ans[cr][cc] = nums[i][j]
                cc += 1

        return ans


