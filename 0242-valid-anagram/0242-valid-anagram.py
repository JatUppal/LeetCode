from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = Counter(s)
        count2 = Counter(t)
        longer = s; 
        if len(s) < len(t):
            longer = t;
        for char in longer:
            if (char not in count2 or count1[char] != count2[char]):
                return False
        return True