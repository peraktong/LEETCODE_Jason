class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we only need to count the number of 1-0 until one array
        count = 0
        ans = 0
        data = {0: 0}
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            if count in data:
                ans = max(ans, i - data[count] + 1)
            else:
                data[count] = i + 1
        return ans




