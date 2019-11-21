class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        res = []
        for i in xrange(len(nums) - 1):
            res.append(self.generateRange(nums[i], nums[i + 1]))
        return [x for x in res if x]

    def generateRange(self, l, r):
        if l == r or l + 1 == r:
            return ""
        if l + 2 == r:
            return str(l + 1)
        return str(l + 1) + "->" + str(r - 1)

    def findMissingRanges(self, nums, lower, upper):
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        res = []
        for i in xrange(len(nums) - 1):
            if nums[i + 1] - nums[i] == 2:
                res.append(str(nums[i] + 1))
            elif nums[i + 1] - nums[i] > 2:
                res.append(str(nums[i] + 1) + "->" + str(nums[i + 1] - 1))
        return res

