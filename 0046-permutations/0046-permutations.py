class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i : int):
            if i == len(nums):
                return res.append(nums.copy())
            for j in range(i, len(nums)):
                # Swap (make change)
                nums[i], nums[j] = nums[j], nums[i]
                # Recurse
                backtrack(i + 1)
                # Undo change
                nums[i], nums[j] = nums[j], nums[i]
        backtrack(0)
        return res