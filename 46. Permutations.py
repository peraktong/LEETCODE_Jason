class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking:

        def backtracking(first=0):
            if first == n:
                ans.append(nums[:])
            for i in range(first, n):
                # in the current permutation:
                nums[first], nums[i] = nums[i], nums[first]
                # use next integer to finish the permutations
                backtracking(first + 1)
                # backtrack: switch i and first back:
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        ans = []
        backtracking()
        return ans





