class Solution:
    def compress(self, chars: list[str]) -> int:
        cur = ''
        n = cnt = i = 0
        chars.append("")
        for c in chars:
            if c == cur:
                n += 1
            else:
                if cur:
                    chars[i] = cur
                    i += 1
                    cnt += 1
                    if n > 1:
                        s = str(n)
                        for j in range(len(s)):
                            chars[i] = s[j]
                            i += 1
                        cnt += len(s)

                cur = c
                n = 1

        return cnt
