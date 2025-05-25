class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = [1] * len(nums)
        count = 0
        for i in range(len(nums)):
            if i == 0:
                continue
            elif (nums[i] - nums[i - 1] == 1):
                longest[count] += 1
            elif (nums[i] - nums[i - 1] != 0):
                count += 1
        longest.sort(reverse=True)
        if longest:
            return longest[0]
        else:
            return 0