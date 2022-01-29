from collections import defaultdict


class Logger:
    def __init__(self):
        self.ttl = defaultdict(lambda: -10)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.ttl[message] + 10 <= timestamp:
            self.ttl[message] = timestamp
            return True

        return False
