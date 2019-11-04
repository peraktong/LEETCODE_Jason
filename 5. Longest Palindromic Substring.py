s = "babad"


class Solution:
    def greedy(self, s, l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # remember we add -1 to l and 1 to r so we return l+1 and r+1-1=r
        return s[l + 1:r]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res = max(self.greedy(s, i, i), self.greedy(s, i, i + 1), res, key=len)
        print(res)
        return res

model =Solution()
model.longestPalindrome(s=s)