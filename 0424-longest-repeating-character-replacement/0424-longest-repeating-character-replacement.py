class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to keep track of character frequencies
        # inside the current sliding window
        count = {}
        # Stores the maximum length of a valid window found so far
        res = 0
        # Left pointer of the sliding window
        left = 0
        # Tracks the highest frequency of any single character
        # in the current window
        maxf = 0
        # Right pointer expands the window one character at a time
        for right in range(len(s)):
            # Add the current character to the frequency map
            count[s[right]] = 1 + count.get(s[right], 0)
            # Update max frequency seen in the window
            maxf = max(maxf, count[s[right]])
            # If replacements needed exceed k, shrink window
            # replacements needed = window size - max frequency
            while (right - left + 1) - maxf > k:
                # Remove the left character from the window
                count[s[left]] -= 1
                left += 1
            # Update result with the largest valid window size
            res = max(res, (right - left) + 1)
        # Return the length of the longest valid substring
        return res