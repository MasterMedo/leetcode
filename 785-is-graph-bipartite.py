from collections import deque, defaultdict


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        arr = [None] * len(graph)
        arr[0] = True
        stack = deque(enumerate(graph))
        last_change = 1
        changes = defaultdict(int)
        while stack:
            i, vertices = stack.popleft()
            if not vertices:
                continue

            elif arr[i] is not None:
                last_change += 1
                for j in vertices:
                    if arr[i] == arr[j]:
                        return False

                    arr[j] = not arr[i]

            elif changes[i] < last_change:
                stack.append((i, vertices))
                changes[i] = last_change

            else:
                stack.appendleft((i, vertices))
                arr[i] = True

        return True
