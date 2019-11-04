class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            if sum([1 for s in strs if shortest[i] != s[i]]) > 0:
                return shortest[:i]
        return shortest
