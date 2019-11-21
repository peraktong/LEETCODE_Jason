class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Let's solve this in a mathematical way
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)
