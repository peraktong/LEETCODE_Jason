class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        acc = 0
        mapping = {0: -1}
        for i, n in enumerate(nums):
            acc += n
            if acc not in mapping:
                mapping[acc] = i
            if acc - k in mapping:
                ans = max(ans, i - mapping[acc - k])
        return ans


