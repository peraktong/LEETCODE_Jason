class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        def helper(x):
            return x == x[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pairs = []
        for word, k in words.iteritems():
            n = len(word)
            for i in range(n + 1):
                p1 = word[:i]
                p2 = word[i:]
                if helper(p1):
                    b = p2[::-1]
                    if b != word and b in words:
                        valid_pairs.append([words[b], k])
                if i != n and helper(p2):
                    b = p1[::-1]
                    if b != word and b in words:
                        valid_pairs.append([k, words[b]])
        return valid_pairs




