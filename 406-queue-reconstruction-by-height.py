class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))

        res = []
        for h, n in people:
            res.insert(n, [h, n])

        return res
