class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        e = ret = 0
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)

        for s in range(len(start)):
            # go through: If conflict, we need a new meet room:
            if start[s] < end[e]:
                ret += 1
            # move to next end time: This means we finish the meeting:
            else:
                e += 1
        return ret
