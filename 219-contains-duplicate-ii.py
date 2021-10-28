from collections import deque


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        roll = deque(maxlen=k)
        seen = set()
        for n in nums:
            if n in seen:
                return True

            if len(roll) == roll.maxlen:
                seen.remove(roll.popleft())
                roll.append(n)
            else:
                roll.append(n)

            seen.add(n)

        return False
