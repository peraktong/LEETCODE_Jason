class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        one, two = nums[:], nums[:]
        # modify pair 1 or 2:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)
