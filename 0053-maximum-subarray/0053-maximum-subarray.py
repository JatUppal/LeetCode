class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-infinity")
        curr = 0
        for n in nums:
            curr += n
            if curr < n:
                curr = n
            res = max(curr, res)
        return res