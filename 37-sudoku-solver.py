from collections import deque
from itertools import chain


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def constraints(visit):
            log = deque()
            while True:
                while visit:
                    r, c = visit.popleft()
                    digit = board[r][c]
                    row = ((r, c_) for c_ in range(9))
                    column = ((r_, c) for r_ in range(9))
                    block = (
                        (r_, c_)
                        for r_ in range(r // 3 * 3, r // 3 * 3 + 3)
                        for c_ in range(c // 3 * 3, c // 3 * 3 + 3)
                    )
                    for r_, c_ in set(chain(row, column, block)):
                        if (r_, c_) != (r, c) and digit in board[r_][c_]:
                            if board[r_][c_] == digit:
                                return False, log

                            board[r_][c_] = board[r_][c_].replace(digit, "")
                            log.append((r_, c_, digit))

                            if len(board[r_][c_]) == 1:
                                visit.append((r_, c_))
                return True, log

        def dfs():
            try:
                r, c = next(iter(sorted((
                    (r, c) for r in range(9)
                    for c in range(9) if len(board[r][c]) > 1
                ), key=lambda t: len(board[t[0]][t[1]]))))
            except StopIteration:
                return True

            digits = board[r][c]
            for digit in digits:
                board[r][c] = digit
                success, log = constraints(deque([(r, c)]))
                if success and dfs():
                    return True

                while log:
                    r_, c_, d_ = log.pop()
                    board[r_][c_] += d_

            board[r][c] = digits
            return False

        visit = deque()
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    board[r][c] = "123456789"
                else:
                    visit.append((r, c))

        constraints(visit)
        dfs()
