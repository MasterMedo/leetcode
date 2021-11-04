class Solution:
    def grayCode(self, n: int) -> List[int]:
        def dfs(start: int):
            nonlocal seen, path
            if len(path) >= 2 ** n:
                return (start & (start - 1)) == 0

            for edge in map(lambda i: 1 << i, range(n)):
                end = start ^ edge
                if end not in seen:
                    seen.add(end)
                    path.append(end)
                    if dfs(end):
                        return True

                    seen.remove(end)
                    del path[-1]

            return False

        path = [0]
        seen = {0}
        dfs(start=0)
        return path
