class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(queens, rows, depth):
            result = 0
            for i in range(n):
                if i in rows:
                    continue

                if all(abs(i - x) != abs(depth - y) for x, y in queens):
                    if depth >= n - 1:
                        return 1
                    else:
                        result += dfs(
                            queens | {(i, depth)},
                            rows | {i},
                            depth + 1,
                        )

            return result

        return dfs(set(), set(), 0)
