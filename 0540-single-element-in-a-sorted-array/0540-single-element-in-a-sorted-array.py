class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # If there's only one element, it must be the answer
        if len(nums) < 2:
            return nums[0]
        # Binary search boundaries
        l, r = 0, len(nums) - 1
        # Continue until search space narrows to one element
        while l < r:
            mid = (l + r) // 2
            # Ensure mid is even so it points to the first element of a pair
            if mid % 2 == 1:
                mid -= 1
            # If this pair is valid, the single element is to the right
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            # Otherwise, the single element is at mid or to the left
            else:
                r = mid
        # l points to the single non-duplicate element
        return nums[l]