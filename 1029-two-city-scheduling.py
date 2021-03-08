class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
        left = right = len(costs) // 2
        cost = 0
        for a, b in costs:
            if left <= 0:
                cost += b
            elif right <= 0:
                cost += a
            else:
                if a < b:
                    cost += a
                    left -= 1
                else:
                    cost += b
                    right -= 1

        return cost
