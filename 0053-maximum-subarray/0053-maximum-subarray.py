class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-infinity")
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr < nums[i]:
                curr = nums[i]
            res = max(res, curr)
        return res