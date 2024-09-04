class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteriod in asteroids:
            if asteriod > mass:
                return False
            else:
                mass = mass + asteriod

        return True
        