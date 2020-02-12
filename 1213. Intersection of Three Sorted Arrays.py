from collections import deque


class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        ans = list(set(arr1) & set(arr2) & set(arr3))
        ans.sort()

        return ans

