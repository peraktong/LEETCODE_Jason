class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        m = len(image)
        n = len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image

        # DFS

        def dfs(i, j):
            if image[i][j] == color:
                # only search this color
                image[i][j] = newColor
                if i > 0:
                    dfs(i - 1, j)
                if i < m - 1:
                    dfs(i + 1, j)
                if j > 0:
                    dfs(i, j - 1)
                if j < n - 1:
                    dfs(i, j + 1)

        dfs(sr, sc)
        return image


