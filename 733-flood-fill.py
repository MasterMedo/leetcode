from collections import deque


class Solution:
    def floodFill(self, image: list[list[int]], r: int, c: int, new: int) -> list[list[int]]:
        old = image[r][c]
        if old == new:
            return image
        image[r][c] = new
        visit = deque([(r, c)])
        while visit:
            r, c = visit.pop()
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == old:
                    image[nr][nc] = new
                    visit.append((nr, nc))

        return image
