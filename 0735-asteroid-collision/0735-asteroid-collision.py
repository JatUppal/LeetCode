class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            alive = True
            if a < 0 and len(res) > 0:
                while alive and len(res) > 0 and res[-1] > 0:
                    if -a > res[-1]:
                        del res[-1]
                    elif -a < res[-1]:
                        alive = False
                    else:
                        alive = False
                        del res[-1]
            if alive:
                res.append(a)
        return res