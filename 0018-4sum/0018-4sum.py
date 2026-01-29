class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()  # Sort so we can use two pointers and skip duplicates easily
        n = len(nums)
        # Pick the 1st number
        for i in range(n - 3):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Pick the 2nd number
            for j in range(i + 1, n - 2):
                # Skip duplicate values for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Now solve 2-sum on the remaining range with two pointers
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        # Found one valid quadruplet
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        # Move pointers inward
                        left += 1
                        right -= 1
                        # Skip duplicates for left
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # Skip duplicates for right
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        # Need a larger sum -> move left up to increase total
                        left += 1
                    else:
                        # Need a smaller sum -> move right down to decrease total
                        right -= 1
        return res  