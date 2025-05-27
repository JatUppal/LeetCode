class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if maxArea < area:
                maxArea = area
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return maxArea