class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        ships = 0
        for y in range(len(board)):
            for x in range(len(board[0])):
                if x > 0 and board[y][x-1] == 'X' \
                        or y > 0 and board[y-1][x] == 'X':
                    continue
                if board[y][x] == 'X':
                    ships += 1

        return ships
