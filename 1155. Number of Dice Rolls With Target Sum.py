class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        self.ans = 0

        def helper(i, rest):
            if i == d:
                if rest == 0:
                    self.ans += 1
                    return
                else:
                    return
            temp = rest
            for m in range(1, min(f + 1, temp + 1)):
                helper(i + 1, rest - m)

        for t in range(1, f + 1):
            helper(1, target - t)

        return self.ans

# DP + memorization:
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        # memorization DP
        memo = {}

        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            if (d, target) in memo:
                return memo[(d, target)]
            to_return = 0
            for k in range(max(0, target - f), target):
                to_return += dp(d - 1, k)
            memo[(d, target)] = to_return
            return to_return

        return dp(d, target) % (10 ** 9 + 7)







