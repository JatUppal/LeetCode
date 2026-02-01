from collections import Counter
class Solution:
     def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = {}
        window = Counter()
        l = 0
        res = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if r - l + 1 > minSize:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            if r - l + 1 == minSize:
                if len(window) <= maxLetters:
                    substring = s[l : r + 1]
                    freq[substring] = freq.get(substring, 0) + 1
                    res = max(res, freq[substring])
        return res