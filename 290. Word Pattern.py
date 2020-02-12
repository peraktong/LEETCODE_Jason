class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        temp = {}
        temp_2 = {}
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        for i in range(len(pattern)):
            if pattern[i] in temp:
                if temp[pattern[i]] != str[i]:
                    return False
            else:
                temp[pattern[i]] = str[i]

            if str[i] in temp_2:
                if temp_2[str[i]] != pattern[i]:
                    return False
            else:
                temp_2[str[i]] = pattern[i]

        return True

