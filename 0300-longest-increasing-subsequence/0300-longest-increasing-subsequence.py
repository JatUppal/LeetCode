class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[i] stores the smallest possible ending value
        # of an increasing subsequence of length i + 1
        tails = []
        # Iterate through each number in the array
        for x in nums:
            # Binary search on tails to find position for x
            l, r = 0, len(tails)
            while l < r:
                mid = (l + r) // 2
                # If x is larger, it can extend a longer subsequence
                if x > tails[mid]:
                    l = mid + 1
                # Otherwise, try to replace a larger value
                else:
                    r = mid
            # If x extends the longest subsequence so far
            if l == len(tails):
                tails.append(x)
            # Otherwise, replace the tail to keep it minimal
            else:
                tails[l] = x
        # Length of tails equals length of LIS
        return len(tails)