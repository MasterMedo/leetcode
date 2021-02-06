from collections import defaultdict, deque


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        tickets.sort(key=lambda t: t[1])
        edges = defaultdict(deque)
        for start, end in tickets:
            edges[start].append(end)

        stack = deque()
        start = 'JFK'
        itinerary = []
        while True:
            while not edges[start]:
                itinerary.append(start)
                if not stack:
                    return itinerary[::-1]
                start = stack.pop()

            stack.append(start)
            start = edges[start].popleft()
