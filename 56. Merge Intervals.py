import collections

array_1 =[[1,3],[8,10],[2,6],[15,18]]



def merge_interval(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for i in intervals:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1], i[1])
    return merged






"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = []
        for i in intervals:
            if not ans or i[0]>ans[-1][1]:
                ans.append(i)
            else:
                ans[-1][1] = max(i[1],ans[-1][1])
        return ans
        
        
"""


merge_interval(intervals=array_1)
