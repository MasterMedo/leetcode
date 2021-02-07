class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        permutations = ['']
        for digit in digits:
            new = []
            for permutation in permutations:
                for c in phone[digit]:
                    new.append(permutation + c)
            permutations = new

        return permutations if permutations[0] else []
