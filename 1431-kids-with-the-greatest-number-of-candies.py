class Solution:
    def kidsWithCandies(self, kids: list[int], candies: int) -> list[bool]:
        max_kid = max(kids)
        return [kid + candies >= max_kid for kid in kids]
