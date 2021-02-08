from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        visit = deque([('', 0, 0)])
        output = []
        seen = {''}
        while visit:
            s, opened, closed = visit.pop()
            if opened < n:
                new = s + '('
                if new not in seen:
                    seen.add(new)
                    visit.append((new, opened + 1, closed))
            if closed < opened:
                new = s + ')'
                if new not in seen:
                    seen.add(new)
                    if closed + 1 >= n:
                        output.append(new)
                    else:
                        visit.append((new, opened, closed + 1))
        return output
