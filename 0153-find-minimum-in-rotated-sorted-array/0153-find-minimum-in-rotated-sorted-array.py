class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        elif len(nums) <= 2:
            return min(nums[0], nums[1])
        res = math.inf
        l, r = 0, len(nums) - 1
        mid = ((l + r) // 2)
        if nums[mid] < nums[r]:
            start = l
            end = mid
        else:
            start = mid
            end = r
        while start <= end:
            if res > nums[start]:
                res = nums[start]
            start += 1
        return res
        
        