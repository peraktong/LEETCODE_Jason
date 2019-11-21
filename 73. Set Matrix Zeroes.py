matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]


class Solution(object):
    def setZeroes(self, matrix):

        # inplace:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i] = ["0" if x != 0 else 0 for x in matrix[i]]
                    for t in range(m):
                        matrix[t][j] = "0" if matrix[t][j] != 0 else 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0

        return matrix