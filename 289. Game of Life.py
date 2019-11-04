class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # die 0,1,4;
        # Do inplace is simple, you can add a big number eg 5 to the number if the status changes.
        rows, cols = len(board), len(board[0])

        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for row in range(rows):
            for col in range(cols):
                n_live = 0
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]
                    if (r >= 0 and r < rows) and (c >= 0 and c < cols) and abs(board[r][c]) == 1:
                        n_live += 1
                if (n_live > 3 or n_live < 2) and board[row][col] == 1:
                    board[row][col] = -1
                if (n_live == 3) and board[row][col] == 0:
                    board[row][col] = 2
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0






