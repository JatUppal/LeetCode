class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        new = string[::-1]
        return string == new