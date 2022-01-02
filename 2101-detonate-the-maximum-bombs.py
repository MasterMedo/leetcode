class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        detonations = [[] for _ in range(len(bombs))]
        for i, (x, y, r) in enumerate(bombs):
            for j, (z, w, _) in enumerate(bombs):
                if sqrt(abs(x - z)**2 + abs(y - w)**2) <= r:
                    detonations[i].append(j)

        best = 0
        memoize = {}
        for bomb in range(len(bombs)):
            detonated = {bomb}
            to_detonate = [bomb]
            while to_detonate:
                i = to_detonate.pop()
                for j in detonations[i]:
                    if j in memoize:
                        detonated |= memoize[j]
                        continue

                    if j not in detonated:
                        detonated.add(j)
                        to_detonate.append(j)

            memoize[bomb] = detonated
            best = max(best, len(detonated))

        return best
