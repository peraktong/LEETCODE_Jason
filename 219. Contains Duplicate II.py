class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # harsh table: data[num[i]]=max_index
        if not nums:
            return False

        data = {}
        N = len(nums)
        for i in range(N):
            temp = data.get(nums[i], -1)
            if temp >= 0 and abs(i - temp) <= k:
                return True
            data[nums[i]] = i
        return False



