class Solution:
    def productExceptSelf(self, arr: list[int]) -> list[int]:
        front = [1]
        back = [1]
        for i in range(len(arr) - 1):
            front.append(front[i] * arr[i])
            back.append(back[i] * arr[-i - 1])

        return [a * b for a, b in zip(front, reversed(back))]
