from heapq import heappush, heappop


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if word[0] == cell:
                    if len(word) == 1:
                        return True

                    visit = [(-1, r, c, frozenset({(r, c)}))]
                    while visit:
                        i, pr, pc, seen = heappop(visit)
                        i = -i
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = pr + dr, pc + dc
                            if (
                                0 <= nr < len(board)
                                and 0 <= nc < len(board[0])
                                and board[nr][nc] == word[i]
                                and (nr, nc) not in seen
                            ):
                                if i + 1 >= len(word):
                                    return True

                                heappush(visit, (-i - 1, nr, nc, seen | {(nr, nc)}))
        return False
