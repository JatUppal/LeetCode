class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        j = 0
        while True:
            if j < len(arr) and arr[j] == i:
                j += 1
            else:
                k -= 1
                if k == 0:
                    return i
            i += 1