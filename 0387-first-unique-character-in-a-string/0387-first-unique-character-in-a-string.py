class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = []
        for char in s:
            if char in seen:
                continue
            if s.count(char) == 1:
                return s.index(char)
            seen.append(char)
        return -1