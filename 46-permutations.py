class Solution:
    def permute(self, arr: list[int]) -> list[list[int]]:
        if len(arr) <= 1:
            return [arr]
        if len(arr) == 2:
            return [arr, arr[::-1]]

        element = arr[0]
        sub_permutations = self.permute(arr[1:])
        permutations = []
        for permutation in sub_permutations:
            permutations.append(permutation + [element])
            for i in range(len(permutation)):
                permutations.append(permutation[:i] + [element] + permutation[i:])
        return permutations
