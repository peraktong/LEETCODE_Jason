class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = {}
        for i in range(len(s)):
            temp[s[i]] = temp.get(s[i], 0) + 1
        ans = 0
        odd_array = []
        for i in temp:
            if temp[i] % 2 == 0:
                ans += temp[i]
            else:
                odd_array.append(temp[i])
        return ans + sum(odd_array) - len(odd_array) + 1 if len(odd_array) > 0 else ans


