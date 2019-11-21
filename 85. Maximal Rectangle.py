class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # DP to store max width
        ans = 0
        dp = [[0] * len(matrix[0]) for x in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    # start next loop
                    continue
                # calculate the max width
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

                # compute the max area with a lower right corner [i,j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    ans = max(ans, width * (i - k + 1))
        return ans


