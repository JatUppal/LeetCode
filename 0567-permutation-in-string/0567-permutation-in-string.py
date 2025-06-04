from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1) - 1
        countS = Counter(s1)
        while right < len(s2):
            countW = Counter(s2[left : right + 1])
            if countS == countW:
                return True
            left += 1
            right += 1
        return False