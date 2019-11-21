"""

The stack maintain the indexes of buildings with ascending
 height. Before adding a new building pop the building who
  is taller than the new one. The building popped out
  represent the height of a rectangle with the new building
   as the right boundary and the current stack top as the left boundary.
   Calculate its area and update ans of maximum area. Boundary is handled using dummy buildings.
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # stack remember the index of ascending order
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                # pop out as right boundary
                # remember it's in ascending order and h is smallest
                h = heights[stack.pop()]
                # width
                width = i - stack[-1] - 1
                ans = max(ans, h * width)
            # use current as hat
            stack.append(i)
        # heights.pop()

        return ans


