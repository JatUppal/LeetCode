class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float("-inf")
        curr = 0
        for x in nums:
            curr = max(curr + x, x)
            if curr > best:
                best = curr
        return best