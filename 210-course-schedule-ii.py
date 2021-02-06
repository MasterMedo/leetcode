class Solution:
    def findOrder(self, n: int, prerequisites: list[list[int]]) -> list[int]:
        def dfs(i):
            nonlocal visit, graph, path
            if visit[i] == -1:
                return False

            if visit[i] == 1:
                return True

            visit[i] = -1
            if all(map(dfs, graph[i])):
                visit[i] = 1
                path.append(i)
                return True

            return False

        graph = [[] for _ in range(n)]
        visit = [0] * n
        path = []
        for x, y in prerequisites:
            graph[x].append(y)

        return path if all(map(dfs, range(n))) else []
