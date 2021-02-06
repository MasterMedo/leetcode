class Solution:
    def canFinish(self, n: int, prerequisites: list[list[int]]) -> bool:
        def dfs(i):
            nonlocal visit, graph
            if visit[i] == -1:
                return False

            if visit[i] == 1:
                return True

            visit[i] = -1
            if all(map(dfs, graph[i])):
                visit[i] = 1
                return True

            return False

        graph = [[] for _ in range(n)]
        visit = [0] * n
        for x, y in prerequisites:
            graph[x].append(y)

        return all(map(dfs, range(n)))
