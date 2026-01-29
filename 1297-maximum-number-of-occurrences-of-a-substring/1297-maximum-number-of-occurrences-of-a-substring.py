class Solution:
     def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # Key observation:
        # We only need to check substrings of length minSize.
        # If a longer substring is valid, its minSize prefix will also be counted,
        # and longer substrings are strictly fewer in number.
        
        n = len(s)
        freq = defaultdict(int)   # counts how many times each valid substring appears
        count = defaultdict(int)  # counts chars in the current sliding window
        unique = 0                # number of unique chars currently in the window
        best = 0                  # max frequency seen so far

        left = 0

        # Expand the window with right pointer
        for right in range(n):
            # Add s[right] into the window
            ch = s[right]
            if count[ch] == 0:
                unique += 1
            count[ch] += 1

            # Keep window size at most minSize (slide forward when too big)
            if right - left + 1 > minSize:
                left_ch = s[left]
                count[left_ch] -= 1
                if count[left_ch] == 0:
                    unique -= 1
                left += 1

            # When window size is exactly minSize, check constraints
            if right - left + 1 == minSize:
                # Only count this substring if it has <= maxLetters unique chars
                if unique <= maxLetters:
                    sub = s[left:right + 1]
                    freq[sub] += 1
                    best = max(best, freq[sub])  # update answer immediately

        return best


