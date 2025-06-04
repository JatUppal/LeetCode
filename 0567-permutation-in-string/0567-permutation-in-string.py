from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        countS1 = Counter(s1)
        window = Counter(s2[:len1])

        if window == countS1:
            return True

        for i in range(len1, len2):
            start_char = s2[i - len1]
            new_char = s2[i]

            window[new_char] += 1
            window[start_char] -= 1
            if window[start_char] == 0:
                del window[start_char]

            if window == countS1:
                return True

        return False
