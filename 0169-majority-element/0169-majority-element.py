class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        target = len(nums) // 2
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if count[num] > target:
                return num
