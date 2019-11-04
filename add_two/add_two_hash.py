import numpy as np
nums = [2, 7, 11, 15]
target = 9
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}

        for i in range(0,len(nums)):
            hash_table[nums[i]]=i
        # print(hash_table)


model = Solution()
results = model.twoSum(nums=nums,target=target)
print(results)