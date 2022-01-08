class Solution:
    def asteroidsDestroyed(self, planet: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if planet < asteroid:
                return False
            planet += asteroid

        return True
