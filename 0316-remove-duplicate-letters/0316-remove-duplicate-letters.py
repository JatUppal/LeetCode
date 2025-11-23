class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s) 
        stack = []    
        in_stack = set()  
        
        for c in s:
            freq[c] -= 1

            if c in in_stack:
                continue

            while stack and c < stack[-1] and freq[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)
            stack.append(c)
            in_stack.add(c)

        return "".join(stack)