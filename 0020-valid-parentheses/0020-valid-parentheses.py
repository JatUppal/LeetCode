class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if c in pair.values():
                stack.append(c)
            elif c in pair.keys():
                if not stack or stack.pop() != pair[c]:
                    return False
            else:
                return False
        return not stack