class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = {-1 : 0}
        for i in range(len(nums)):
            prefix[i] = nums[i] + prefix[i - 1]
        return list(prefix.values())[1:]