import heapq


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)
        ans = float("-inf"), float("inf")
        # Use the max as right
        right = max(row[0] for row in nums)
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(nums[i]):
                # This means we scan all this list
                return ans
            v = nums[i][j + 1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j + 1))


