from collections import deque, Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen = Counter()
        ask = Counter(t)
        sub = deque()
        best_i = -1
        best = float("inf")
        for i, c in enumerate(s):
            seen[c] += 1
            sub.append(c)
            if seen[c] == ask[c] and all(seen[a] >= ask[a] for a in ask):
                while True:
                    a = sub[0]
                    if seen[a] == ask[a]:
                        break

                    sub.popleft()
                    seen[a] -= 1
                if len(sub) < best:
                    best = len(sub)
                    best_i = i - len(sub) + 1
                seen[sub.popleft()] -= 1

        if best_i == -1:
            return ""
        else:
            return s[best_i : best_i + best]
