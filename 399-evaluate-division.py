from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        table = defaultdict(lambda: defaultdict(lambda: -1))
        visit = deque()
        for (a, b), n in zip(equations, values):
            table[a][b] = n
            table[b][a] = 1 / n
            visit.append((a, b, n))
            visit.append((b, a, 1 / n))

        while visit:
            start, a, n = visit.popleft()
            for end in table[a]:
                if end not in table[start]:
                    rate = n * table[a][end]
                    table[start][end] = rate
                    table[end][start] = 1 / rate
                    visit.append((start, end, rate))
                    visit.append((end, start, 1 / rate))

        return [table[a][b] for a, b in queries]
