from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                  47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

        anagrams = defaultdict(list)
        for s in strs:
            product = 1
            for c in s:
                product *= primes[ord(c) - 97]
            anagrams[product].append(s)

        return list(anagrams.values())
