from collections import deque


class Solution:
    def kSimilarity(self, a: str, b: str) -> int:
        if a == b:
            return 0

        visit = deque([a])
        seen = {a: 0}
        while visit:
            a = visit.popleft()
            la = list(a)
            i = next(i for i in range(len(a)) if a[i] != b[i])
            for j in range(i + 1, len(a)):
                if la[i] != la[j] and la[i] == b[j]:
                    la[i], la[j] = la[j], la[i]
                    a_ = ''.join(la)
                    if a_ not in seen:
                        if a_ == b:
                            return seen[a] + 1

                        seen[a_] = seen[a] + 1
                        visit.append(a_)
                    la[i], la[j] = la[j], la[i]
