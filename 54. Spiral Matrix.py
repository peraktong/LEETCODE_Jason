"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return None
        N_r=len(matrix)-1
        N_c=len(matrix[0])-1
        row = 0
        col = 0
        ans = []
        while row<N_r-row and col<N_c-col:
            m1= matrix[row][col:N_c-col+1]
            m2= [x[N_c-col] for x in matrix[row:N_r-row+1]]
            m3= matrix[N_r-row][col:N_c-col+1][::-1]
            m4= [x[col] for x in matrix[row:N_r-row+1]][::-1]
            ans.extend(m1)
            ans.extend(m2)
            ans.extend(m3)
            ans.extend(m4)
        return ans

"""


class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        row = len(matrix)
        col = len(matrix[0])
        seen = [[False] * col for n in matrix]
        ans = []
        r = c = di = 0
        # for r: 1 means we move from row to row+1:first round
        dr = [0, 1, 0, -1]
        # for 1: it means we move one right for the column: for -1, it means we move from round 2 to ropund 3
        dc = [1, 0, -1, 0]
        for n in range(row * col):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if (cr >= 0 and cr < row) and (cc >= 0 and cc < col) and not seen[cr][cc]:
                # This means we never walk to cr and cc, we can walk from here
                r, c = cr, cc
            else:
                # This means we walk a loop=4
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans



