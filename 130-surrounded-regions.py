class Solution:
    def solve(self, board: List[List[str]]) -> None:
        height = len(board)
        width = len(board[0])
        uncaptured = []
        captured = set()
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == "X":
                    continue
                if r in [0, height - 1] or c in [0, width - 1]:
                    uncaptured.append((r, c))
                    continue
                captured.add((r, c))

        while uncaptured:
            r, c = uncaptured.pop()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in captured:
                    captured.remove((nr, nc))
                    uncaptured.append((nr, nc))

        for r, c in captured:
            board[r][c] = "X"
