"""
# simple way:
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = collections.defaultdict(list)
        # use tuple since it's hashable:
        for s in strs:
            temp[tuple(sorted(s))].append(s)
        return temp.values()




O(NKlogK)


"""