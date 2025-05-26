class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen.keys():
                return [seen[complement] + 1, i + 1]
            seen[num] = i