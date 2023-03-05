from collections import defaultdict


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        paths = defaultdict(lambda: float('inf'))
        paths[0] = triangle[0][0]
        for height in range(1, len(triangle)):
            new_paths = defaultdict(lambda: float('inf'))
            for index in range(len(triangle[height])):
                value = triangle[height][index]
                new_paths[index] = min(
                    paths[index] + value,
                    paths[index - 1] + value,
                )

            paths = new_paths
        return min(paths.values())
