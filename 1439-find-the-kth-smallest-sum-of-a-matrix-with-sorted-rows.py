from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, mat: list[list[int]], k: int) -> int:
        index = tuple([0] * len(mat))
        to_visit = [(sum(row[0] for row in mat), index)]
        visited = set([index])
        for _ in range(k):
            s, index = heappop(to_visit)
            for i in range(len(mat)):
                if index[i] + 1 < len(mat[0]):
                    index_ = tuple(e if j != i else e+1
                                   for j, e in enumerate(index))
                    if index_ not in visited:
                        visited.add(index_)
                        s_ = sum(mat[y][x] for y, x in enumerate(index_))
                        heappush(to_visit, (s_, index_))
        return s
