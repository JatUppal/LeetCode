class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            alive = True
            while alive and a < 0 and stack and stack[-1] > 0:
                if stack[-1] < -a:          # top smaller -> top explodes
                    stack.pop()
                    continue
                elif stack[-1] == -a:       # equal -> both explode
                    stack.pop()
                alive = False               # current explodes (or both did)
            if alive:
                stack.append(a)
        return stack