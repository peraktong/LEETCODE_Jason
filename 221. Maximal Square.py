class Solution(object):
    def maximalSquare(self, matrix):
        

        # use DP?
        # check the edge case:
        # input is str:
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 if matrix[i][j]=="0" else 1 for j in range(col)] for i in range(row)]
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]=="1":
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                else:
                    dp[i][j]=0
        res = max(max(row) for row in dp)
        return res**2
        
        
        