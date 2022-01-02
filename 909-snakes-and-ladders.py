from math import inf
from collections import defaultdict, deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        max_ = len(board) * len(board)
        moves = defaultdict(lambda: -1)
        count = defaultdict(lambda: inf)
        count[1] = 0
        r, c = len(board) - 1, 1
        m = 2
        d = 1
        while r >= 0:
            moves[m] = board[r][c]
            if 0 <= c + d < len(board):
                c += d
            else:
                d *= -1
                r -= 1
            m += 1

        stack = deque([1])
        while stack:
            m = stack.popleft()
            for i in range(1, 7):
                if m + i <= max_:
                    if moves[m + i] == -1:
                        if count[m + i] == inf:
                            count[m + i] = count[m] + 1
                            stack.append(m + i)
                    else:
                        if count[moves[m + i]] == inf:
                            count[moves[m + i]] = count[m] + 1
                            stack.append(moves[m + i])

        return count[max_] if count[max_] != inf else -1
