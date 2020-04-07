class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        # memorization recursive: use harsh table

        if s in memo:
            return memo[s]
        if not s:
            return []
        ans = []
        for w in wordDict:
            n = len(w)
            if not s[:n] == w:
                # The word not in wordDict, we skip this loop
                continue
            if n == len(s):
                ans.append(w)
            else:
                rest = self.helper(s[n:], wordDict, memo)
                for r in rest:
                    r = w + ' ' + r
                    ans.append(r)
        memo[s] = ans
        return ans


