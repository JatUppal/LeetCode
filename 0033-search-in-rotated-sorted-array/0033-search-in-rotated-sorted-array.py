class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = ((l + r) // 2)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        indx = l
        l, r = 0, len(nums) - 1
        if target >= nums[indx] and target <= nums[r]:
            l = indx
        else:
            r = indx - 1
        while l <= r:
            mid = ((l + r) // 2) 
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1