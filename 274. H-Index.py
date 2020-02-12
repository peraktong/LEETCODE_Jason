class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # sorting
        citations.sort()
        i = 0
        while i < len(citations) and citations[len(citations) - i - 1] > i:
            i += 1
        return i
