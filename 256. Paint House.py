class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Let's use DP: paint one house for one color has minimum cost of paint nearby with other two colors:
        for i in reversed(range(len(costs) - 1)):
            costs[i][0] += min(costs[i + 1][1], costs[i + 1][2])
            costs[i][1] += min(costs[i + 1][0], costs[i + 1][2])
            costs[i][2] += min(costs[i + 1][1], costs[i + 1][0])
        if len(costs) == 0:
            return 0
        return min(costs[0])



