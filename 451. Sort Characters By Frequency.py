class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        data = {}
        for char in s:
            data[char] = data.get(char, 0) + 1
        ans = ""
        for i in sorted(data.items(), key=lambda x: x[1], reverse=True):
            ans += i[1] * i[0]

        return ans


