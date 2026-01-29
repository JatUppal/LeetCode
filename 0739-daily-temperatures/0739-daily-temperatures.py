class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)              # Total number of days
        res = [0] * n                      # Result array, default 0 means no warmer day
        stack = []                         # Stack stores indices of unresolved days
        # Loop through each day and temperature
        for i, t in enumerate(temperatures):
            # While there is a previous day waiting for a warmer temperature
            # and today's temperature is warmer than that day
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()            # Resolve that previous day
                res[j] = i - j             # Days waited until a warmer temperature
            # Add current day's index to stack to be resolved later
            stack.append(i)
        # Any index left in stack has no warmer future day, so stays 0
        return res