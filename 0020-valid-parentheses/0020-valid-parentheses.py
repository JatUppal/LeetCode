class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')' : '(', ']' : '[', '}' : '{'}
        stack = []
        for c in s:
            if c in valid:
                if not stack or stack[-1] != valid[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack