def solution(s,k):
    # edge case:
    if len(s) <= k:
        return len(s)
    # naive two pointer
    start = 0
    stop = k
    ans = k

    while stop < len(s):
        temp = s[start:stop]
        stop += 1
        #
        while len(set(s[start:stop])) > k:
            start += 1
        ans = max(ans, stop - start)
    return ans



print(solution(s="eceba",k=2))


## hash table:

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        # edge case:
        if len(s) <= k:
            return len(s)
        # use harsh table

        d = {}
        ans = 0
        lower = 0
        for upper, c in enumerate(s):
            # store the most upper right location for each element, which means before this there must be element c
            d[c] = upper
            if len(d) > k:
                lower = min(d.values())
                del d[s[lower]]
                lower += 1
            ans = max(ans, upper - lower + 1)
        return ans



