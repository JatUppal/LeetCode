class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if left == right:
                return nums[left]
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid +  1
        