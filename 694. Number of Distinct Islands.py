class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # need to store each island:
        # hash by local coordinates:
        seen = set()
        shapes = set()

        def explore(r, c, r0, c0):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] and (r, c) not in seen:
                seen.add((r, c))
                shape.add((r - r0, c - c0))
                explore(r + 1, c, r0, c0)
                explore(r - 1, c, r0, c0)
                explore(r, c + 1, r0, c0)
                explore(r, c - 1, r0, c0)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c, r, c)
                # this means there is at least one island
                if shape:
                    # use frozen set to make sure one shape is one
                    shapes.add(frozenset(shape))
        return len(shapes)









