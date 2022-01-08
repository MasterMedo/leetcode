def update(fenwick_tree, i, delta):
    while i < len(fenwick_tree):
        fenwick_tree[i] += delta
        i += i & -i


def lower_bound(fenwick_tree, taller_in_front, bitMask):
    ans_i = 0
    while bitMask != 0:
        fenwick_i = ans_i + bitMask
        bitMask >>= 1
        if fenwick_i < len(fenwick_tree):
            if taller_in_front > fenwick_tree[fenwick_i]:
                ans_i = fenwick_i
                taller_in_front -= fenwick_tree[fenwick_i]

    return ans_i


class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        if not people:
            return []

        people.sort(key=lambda p: (p[0], -p[1]))
        ans = [0] * len(people)
        fenwick_tree = [0] * (len(people) + 1)
        bitMask = 1
        n = len(people)
        while bitMask * 2 < n:
            bitMask *= 2

        for i in range(2, n + 1):
            update(fenwick_tree, i, 1)

        for people_i in range(n):
            ans_i = lower_bound(fenwick_tree, people[people_i][1], bitMask)
            if ans_i == len(people):
                ans_i -= 1
            ans[ans_i] = people[people_i]
            update(fenwick_tree, ans_i + 1, -1)

        return ans
