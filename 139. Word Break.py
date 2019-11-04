class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # use DP:
        # DP: at index i: we count everthing and find possible dict[word] between 0 to i

        ans = [True]
        for i in range(1, len(s) + 1):
            ans += any(ans[j] and s[j:i] in wordDict for j in range(i)),
        return ans[-1]
