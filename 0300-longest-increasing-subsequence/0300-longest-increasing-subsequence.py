class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        answer = 1
        for i in range(len(nums)):
            for left in range(i):
                if nums[left] < nums[i]:
                    if lis[left] + 1 > lis[i]:
                        lis[i] = lis[left] + 1
            answer = max(lis[i], answer)
        return answer