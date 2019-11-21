class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = set([])
        for n in nums:
            if n in temp:
                return n
            temp.add(n)
