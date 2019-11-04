class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # use residual to check:
        N = len(gas)
        start = 0
        tot = 0
        cur = 0

        for i in range(N):
            tot += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                # pick up next station as start
                start = i + 1
                cur = 0
        return start if tot >= 0 else -1



