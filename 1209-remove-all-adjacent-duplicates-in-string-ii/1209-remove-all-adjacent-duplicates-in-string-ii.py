class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if k > len(s):
            return s
        stack = []
        for i in range(len(s)):
            if stack and stack[-1][0] == s[i]:
                curr = stack[-1][1]
                stack.pop()
                if curr != k - 1:
                    stack.append((s[i], curr + 1))
            else:
                stack.append((s[i], 1))
        return "".join(char * count for char, count in stack)
        