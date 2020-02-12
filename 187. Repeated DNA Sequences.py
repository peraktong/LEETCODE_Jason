class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # use set
        N = len(s)
        ans = set()
        seen = set()
        for i in range(N - 10 + 1):
            temp = s[i:i + 10]
            if temp in seen:
                ans.add(temp[:])
            seen.add(temp)
        return list(ans)

