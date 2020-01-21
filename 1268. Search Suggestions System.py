import bisect


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        # The length of words is decresing vs searchword
        ans = []
        products.sort()
        prefix = ''
        i = 0
        for w in searchWord:
            prefix += w
            i = bisect.bisect_left(products, prefix, i)
            temp = [w for w in products[i:i + 3] if w.startswith(prefix)]
            ans.append(temp)
        return ans



