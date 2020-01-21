import heapq


class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        # always start with lowest since they are added the most
        ans = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            ans += x + y
            heapq.heappush(sticks, x + y)
        return ans

