class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for x in nums:
            l, r = 0, len(tails)
            while l < r:
                mid = (l + r) // 2
                if x > tails[mid]:
                    l = mid + 1
                else:
                    r = mid
            # now l is the position to place x
            if l == len(tails):
                tails.append(x)
            else:
                tails[l] = x
        return len(tails)