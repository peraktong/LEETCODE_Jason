"""
# brutal force:
# time limit exceed:
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_s = sorted(p)
        lp = len(p)

        def helper(x):
            if sorted(x)==p_s:
                return True
            else:
                return False

        # brutal force:
        ans = []
        for i in range(len(s)-lp+1):
            if helper(s[i:i+lp]):
                ans.append(i)
        return ans




"""


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









