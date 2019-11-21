import bisect
from heapq import heappush,heappop
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        """
        # use heapq:
        heapmin = []
        # put the first element of each list into the heap until k:
        for i in range(min(k, len(matrix))):
            heappush(heapmin, (matrix[i][0], 0, matrix[i]))
        # each time we pop the top(min) of the heap and stop when we get kth
        count, num = 0, 0
        while heapmin:
            num, i, row = heappop(heapmin)
            count += 1
            if count == k:
                break
            # If the top element is longer than i, add move to the next element in the matrix:
            if len(row) > i + 1:
                heappush(heapmin, (row[i + 1], i + 1, row))

        return num

        """
        # also try binary search: since the matrix is sorted, we can use bisect:

        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            mid = (high + low) // 2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                low = mid + 1
            else:
                high = mid
        return low





