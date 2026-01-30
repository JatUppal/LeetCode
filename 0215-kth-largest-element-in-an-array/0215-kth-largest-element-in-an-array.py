class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        nums.reverse()
        return nums[k-1]