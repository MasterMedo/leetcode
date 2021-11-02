class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        steps = {0: 0}
        for i in range(amount + 1):
            for coin in coins:
                if i - coin in steps and steps[i - coin] + 1 < steps.get(
                    i, float("inf")
                ):
                    steps[i] = steps[i - coin] + 1

        return steps.get(amount, -1)
