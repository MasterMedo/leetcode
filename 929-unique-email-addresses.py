class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            chars = []
            for c in local:
                if c == '.':
                    continue
                elif c == '+':
                    break
                else:
                    chars.append(c)
            local = ''.join(chars)
            seen.add((local, domain))

        return len(seen)
