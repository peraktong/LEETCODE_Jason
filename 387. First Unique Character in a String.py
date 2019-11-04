import collections
# brutal force
"""

def firstUniqChar(s):
    ans = [s.count(i) for i in s]
    for index, t in enumerate(ans):
        if t==1:
            return index

    return -1
"""

# magic:
# use Harsh table to boost the speed
def firstUniqChar(s):
    count = collections.Counter(s)
    index = 0
    for char in s:
        if count[char]==1:
            return index
        else:
            index += 1
    return -1



print(firstUniqChar(s="leetcode"))