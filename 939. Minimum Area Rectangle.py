import collections


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        ans = float("inf")
        last_x = {}
        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in last_x:
                        ans = min(ans, (x - last_x[y1, y2]) * (y2 - y1))
                    last_x[y1, y2] = x
        return ans if ans < float("inf") else 0



