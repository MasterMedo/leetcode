from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        seen = defaultdict(int)
        need = defaultdict(int)
        for i in range(len(s1)):
            seen[s2[i]] += 1
            need[s1[i]] += 1

        left = sum(need[char] > seen[char] for char in need)
        for i in range(len(s1), len(s2)):
            if left == 0:
                return True

            char = s2[i - len(s1)]
            seen[char] -= 1
            if need[char] == seen[char] + 1:
                left += 1

            char = s2[i]
            seen[char] += 1
            if need[char] == seen[char]:
                left -= 1

        return left == 0
