class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # the length of the world is monotonical increasing:
        dp = {}
        for w in sorted(words,key=len):
            temp = []
            for i in range(len(w)):
                temp.append(dp.get(w[:i]+w[i+1:],0)+1)
            dp[w] = max(temp)
        return max(dp.values())