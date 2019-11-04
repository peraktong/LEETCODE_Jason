class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        # Let's convert to min:
        def helper(x):
            m1, m2 = x.split(":")
            m1 = int(m1)
            m2 = int(m2)
            return (m1 * 60 + m2) % 1440

        minutes = [helper(x) for x in timePoints]
        minutes.sort()
        # The required minimum difference must be a difference between two adjacent elements in the circular array (so the last element is "adjacent" to the first.) We take the minimum value of all of them.
        return min((y - x) % (24 * 60)
                   for x, y in zip(minutes, minutes[1:] + minutes[:1]))

