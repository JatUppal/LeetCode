class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourAngle = (hour % 12) * 30 + (minutes * 0.5)
        minAngle = minutes * 6
        difference = abs(hourAngle - minAngle)
        return min(difference, 360 - difference)
        