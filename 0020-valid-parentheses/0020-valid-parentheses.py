class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            if char in mapping.keys():
                if not stack:
                    return False
                if mapping[char] != stack[-1]:
                    return False
                stack.pop()
        return not stack