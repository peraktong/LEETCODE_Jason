A = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

def island(grid):
    ans = 0
    R, C = len(grid), len(grid[0])
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                if c==0:
                    ans+=1
                elif grid[r][c - 1] == 0:
                    ans+=1

                if c==3:
                    ans+=1
                elif grid[r][c + 1] == 0:
                    ans+=1

                if r == 0:
                    ans += 1
                elif grid[r-1][c] == 0:
                    ans += 1

                if r == 3:
                    ans += 1
                elif grid[r+1][c] == 0:
                    ans += 1

    print(ans)
    return ans
island(grid=A)