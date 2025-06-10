class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char != "+" and char != "-" and char != "*" and char != "/":
                stack.append(char)
            elif stack:
                var1 = stack.pop()
                var2 = stack.pop()
                expr = str(var2) + char + str(var1)
                result = int(eval(expr))
                stack.append(result)
        res = int(stack.pop())
        return res