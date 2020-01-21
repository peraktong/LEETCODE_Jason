"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""


class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        # the order of each employee doesn't matter

        ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        ans, end = [], ints[0].end
        for i in ints[1:]:
            if i.start > end:
                ans.append(Interval(end, i.start))
            end = max(end, i.end)
        return ans


