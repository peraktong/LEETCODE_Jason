class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.data = {}
        for i in range(len(words)):
            w = words[i]
            if w in self.data:
                self.data[w].append(i)
            else:
                self.data[w] = [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ans = float("inf")
        loc1 = self.data[word1]
        loc2 = self.data[word2]
        l1, l2 = 0, 0
        while l1 < len(loc1) and l2 < len(loc2):
            ans = min(ans, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
        return ans

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)