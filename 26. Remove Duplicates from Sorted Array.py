class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointer:
        if not nums:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                # This means we can move i ahead and assign j to ith
                i += 1
                nums[i] = nums[j]

        return i + 1


