class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval[0], newInterval[1]
        i, n = 0, len(intervals)
        ans = []
        # before
        while i < n and new_start > intervals[i][0]:
            ans.append(intervals[i])
            i += 1
        # add new interal
        # no overlap
        if not ans or ans[-1][1] < new_start:
            ans.append(newInterval)
        else:
            ans[-1][1] = max(ans[-1][-1], new_end)

        # add next intervals and merge if needed:
        while i < n:
            interval = intervals[i]
            start, end = interval[0], interval[1]
            i += 1
            if ans[-1][-1] < start:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], end)
        return ans










