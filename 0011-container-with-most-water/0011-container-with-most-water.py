class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = (r - l) * min(height[r], height[l])
            maxArea = max(area, maxArea)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return maxArea