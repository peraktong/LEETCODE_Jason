class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # find f[i+1] and f[i+2]:
        f1 = f2 = 0
        for x in reversed(cost):
            # two step at most
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)
