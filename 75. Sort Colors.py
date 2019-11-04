class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # use one pass:
        # for all idx < p0 : nums[idx < p0] = 0
        # curr is an index of element under consideration

        # use p0 and p2 to split 0-1 and 1-2:
        p0 = 0
        curr = 0
        p2 = len(nums) - 1
        # one scan from 0 to N-1
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                # curr is 1
                curr += 1

