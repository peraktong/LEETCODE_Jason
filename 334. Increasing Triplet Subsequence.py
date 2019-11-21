class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # DP is slow 
        """
        n = len(nums)
        first = float("inf")
        second = float("inf")

        for i in range(n):
            if nums[i] < first:
                first = nums[i]
            elif first < nums[i] < second:
                second = nums[i]
            if nums[i] > second:
                return True

        return False
        
        """

        # fancy!:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False




