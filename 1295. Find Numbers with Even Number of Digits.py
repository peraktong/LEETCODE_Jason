class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def helper(num):
            num = str(num)
            if len(num) % 2 == 0:
                return 1
            else:
                return 0

        ans = 0
        for num in nums:
            ans += helper(num)
        return ans
