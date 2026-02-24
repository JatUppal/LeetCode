class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0 : -1}
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if (curr_sum % k) in prefix:
                if (i - prefix[curr_sum % k]) >= 2:
                    return True
            else:
                prefix[curr_sum % k] = i
        return False