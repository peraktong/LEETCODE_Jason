class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        tot = 0

        row_max = [max(row) for row in grid]
        column_max = [max(col) for col in zip(*grid)]

        for r, row in enumerate(grid):
            for c,value in enumerate(row):
                tot+=min(row_max[r],column_max[c])-value

        return tot



grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
model =Solution()
print(model.maxIncreaseKeepingSkyline(grid=grid))