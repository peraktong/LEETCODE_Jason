from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        n = len(s)
        if n < 3:
            return n
        left, right = 0, 0
        mapping = defaultdict()
        while right < n:
            if len(mapping) < 3:
                mapping[s[right]] = right
                right += 1
            if len(mapping) == 3:
                del_index = min(mapping.values())
                del mapping[s[del_index]]
                left = del_index + 1
            ans = max(ans, right - left)
        return ans

