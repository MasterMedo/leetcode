from threading import Lock


class DiningPhilosophers:
    def __init__(self):
        self.locks = [Lock() for _ in range(5)]

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:

        left = (philosopher - 1) % 5
        right = philosopher
        lo, hi = sorted([left, right])
        with self.locks[lo]:
            with self.locks[hi]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
