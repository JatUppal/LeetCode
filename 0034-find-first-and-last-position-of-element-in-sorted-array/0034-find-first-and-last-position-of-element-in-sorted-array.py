class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums:
            return res
        
        def findleft():
            l = 0
            r = len(nums) - 1
            left = -1
            while l <= r:
                mid = (l + r) // 2
                if target == nums[mid]:
                    left = mid
                    r = mid - 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return left
        
        def findright():
            l = 0
            r = len(nums) - 1
            right = -1
            while l <= r:
                mid = (l + r) // 2
                if target == nums[mid]:
                    right = mid
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return right
        res[0] = findleft()
        res[1] = findright()
        return res