class Solution:
    def isPalindrome(self, s: str) -> bool:
        noSpace = s.replace(" ", "")
        pat = noSpace.lower()
        clean = ''.join(c for c in pat if c.isalnum())
        return clean == clean[::-1]