class Solution:
    def longestValidParentheses(self, s: str) -> int:
        cnt = consecutive = best = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
            else:
                cnt -= 1

            consecutive += 1
            if cnt == 0:
                best = max(best, consecutive)
            elif cnt < 0:
                cnt = consecutive = 0

        cnt = consecutive = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                cnt += 1
            else:
                cnt -= 1

            consecutive += 1
            if cnt == 0:
                best = max(best, consecutive)
            elif cnt < 0:
                cnt = consecutive = 0

        return best
