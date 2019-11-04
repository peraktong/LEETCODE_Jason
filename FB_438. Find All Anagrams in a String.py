class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # time complexity: avoid sorted!
        # hash table O(1)
        # use hash table to check whether it's the same:
        ans = []
        ls = len(s)
        lp = len(p)
        # edge case check:
        if ls < lp:
            return []
        shash, phash = [0] * 128, [0] * 128
        for x in p:
            phash[ord(x)] += 1

        for i in range(ls):
            shash[ord(s[i])] += 1
            # remove i-lp and the start index is i-lp+1
            if i - lp >= 0:
                shash[ord(s[i - lp])] -= 1
            if shash == phash:
                ans.append(i - lp + 1)
        return ans
"""
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # try sliding window

        
        ans = []
        l = len(p)
        cp = Counter(p)
        cs = Counter(s[:l-1])
        i=0
        while i+l<len(s)+1:
            cs[s[i+l-1]]+=1
            if cs==cp:
                ans.append(i)
            cs[s[i]]-=1
            if cs[s[i]]<=0:
                del cs[s[i]]
            i+=1
        return ans
            
        
        
        

"""



