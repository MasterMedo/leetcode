class Solution:
    def totalFruit(self, tree: list[int]) -> int:
        last = last_i = None
        n = m = 0
        current = set()
        for i, e in enumerate(tree):
            if len(current) < 2:
                current.add(e)
                n += 1

            elif e in current:
                n += 1

            else:
                n = i - last_i + 1
                current = {last, e}

            m = max(m, n)

            if last != e:
                last = e
                last_i = i

        return m
