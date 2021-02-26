class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        left = right = cur = 0
        for i, box in enumerate(boxes):
            if box == '1':
                right += 1
                cur += i

        operations = []
        for i, box in enumerate(boxes):
            operations.append(cur)
            if box == '1':
                left += 1
                right -= 1

            cur -= right
            cur += left

        return operations
