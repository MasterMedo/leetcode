from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_m = Counter(magazine)
        count_r = Counter(ransomNote)
        return all(count_r[c] <= count_m[c] for c in count_r)
