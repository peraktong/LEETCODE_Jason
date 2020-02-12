class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        for word in words:
            w = set(word.lower())
            if w <= line1 or w <= line2 or w <= line3:
                ans.append(word)
        return ans


