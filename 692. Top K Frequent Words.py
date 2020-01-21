class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        # sort on two standards
        ans = sorted(d, key=lambda w: (-d[w], w))
        return ans[:k]

