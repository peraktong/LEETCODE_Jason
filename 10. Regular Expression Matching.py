class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # DP:
        # use a memory dictionary to remember patterns
        memory = {}

        def dp(i, j):
            if (i, j) not in memory:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], "."}
                    if j + 1 < len(p) and p[j + 1] == "*":
                        ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memory[i, j] = ans
            return memory[i, j]

        return dp(0, 0)