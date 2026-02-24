class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        curr_sum = 0
        res = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix:
                res += prefix[curr_sum - k]
            prefix[curr_sum] = 1 + prefix.get(curr_sum, 0)
        return res