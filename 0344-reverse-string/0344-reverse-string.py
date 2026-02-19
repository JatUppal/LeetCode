class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            r -= 1
            l += 1