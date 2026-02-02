class Solution:
    # best = 0
    # longest
    # [1, 2, 3, 4, 5, 9, 10, 11, 12]
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        longest = 1
        if len(nums) == 0:
            return best
        number = set(nums)
        numbers = sorted(number)
        for i in range(len(numbers) - 1):
            if (numbers[i] + 1) == numbers[i + 1]:
                longest += 1
            else:
                best = max(longest, best)
                longest = 1
        return max(longest, best)
            
