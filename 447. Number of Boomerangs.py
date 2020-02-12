class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        N = len(points)
        for i in range(N):
            mapping = {}
            for j in range(N):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                mapping[x ** 2 + y ** 2] = 1 + mapping.get(x ** 2 + y ** 2, 0)
            for key in mapping:
                ans += (mapping[key]) * (mapping[key] - 1)
        return ans

