class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            alive = True
            if a < 0:
                while alive and res and res[-1] > 0:
                    if -a > res[-1]:
                        res.pop()
                    elif -a < res[-1]:
                        alive = False
                    else:
                        alive = False
                        res.pop()
            if alive:
                res.append(a)
        return res
        