class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, rows, depth):
            result = []
            for i in range(n):
                if i in rows:
                    continue

                if all(abs(i - x) != abs(depth - y) for x, y in queens):
                    if depth >= n - 1:
                        queens.add((i, depth))
                        for w in range(n):
                            result.append(
                                "".join(
                                    [".", "Q"][(z, w) in queens]
                                    for z in range(n)
                                )
                            )
                        return [result]
                    else:
                        result.extend(
                            dfs(
                                queens | {(i, depth)},
                                rows | {i},
                                depth + 1,
                            )
                        )

            return result

        return dfs(set(), set(), 0)
