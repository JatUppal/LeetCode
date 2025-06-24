class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        elif len(nums) <= 2:
            return min(nums[0], nums[1])
        res = math.inf
        l, r = 0, len(nums) - 1
        while l < r:
            mid = ((l + r) // 2)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            if res > nums[l]:
                res = nums[l]
        return res