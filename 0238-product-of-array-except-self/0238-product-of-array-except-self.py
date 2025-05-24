class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prefix = [0] * (len(nums) + 1)
        prefix[0] = 1
        postfix = [0] * (len(nums) + 1)
        postfix[len(nums)] = 1
        for i, num in enumerate(nums):
            prefix[i + 1] = num * prefix[i]
        for j in range(len(nums) - 1, -1, -1):
            postfix[j] = nums[j] * postfix[j + 1]
        for i, num in enumerate(prefix):
            if i != len(nums):
                res[i] = num * postfix[i + 1]
        return res