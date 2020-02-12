class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        ans = 0
        for c in count:
            if c + 1 in count:
                ans = max(ans, count[c] + count[c + 1])
        return ans
