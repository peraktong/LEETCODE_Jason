class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = {}
        for i in range(len(s)):
            temp[s[i]] = temp.get(s[i], 0) + 1
        count = 0
        # count odd number
        for t in temp:
            if temp[t] % 2 != 0:
                count += 1
        if len(s) % 2 == 0:
            if count == 0:
                return True
            else:
                return False
        elif len(s) % 2 == 1:
            if count == 1:
                return True
            else:
                return False

