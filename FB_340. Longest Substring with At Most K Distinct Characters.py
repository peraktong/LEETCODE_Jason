class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # always check the edge case:
        if len(s) < k:
            return len(s)
        # two pointer?
        dict_s = {}
        ans = 0
        lower = 0
        for upper, char in enumerate(s):
            # Find the max index for each char in s:
            dict_s[char] = upper
            if len(dict_s) > k:
                lower = min(dict_s.values())
                del dict_s[s[lower]]
                lower += 1
            ans = max(ans, upper - lower + 1)
        return ans



