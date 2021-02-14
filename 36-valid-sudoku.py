class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for x in range(9):
            col = [board[x][y] for y in range(9) if board[x][y] != '.']
            if len(col) != len(set(col)):
                return False

            row = [board[y][x] for y in range(9) if board[y][x] != '.']
            if len(row) != len(set(row)):
                return False

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                sub = [board[r + x][c + y] for x in range(3) for y in range(3) if board[r + x][c + y] != '.']
                if len(sub) != len(set(sub)):
                    return False

        return True
