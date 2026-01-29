class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)

        # Backtracking over "where to cut" the next number and which operator to place.
        # idx  = current index in num we still need to use
        # expr = expression string built so far
        # cur  = evaluated value of expr so far
        # last = the last operand value added to cur (used to fix precedence for '*')
        def dfs(idx: int, expr: str, cur: int, last: int) -> None:
            # If we've used all digits, check if we hit the target
            if idx == n:
                if cur == target:
                    res.append(expr)
                return
            # Try every possible next chunk num[idx:j+1]
            for j in range(idx, n):
                # No leading zeros: if the chunk starts with '0', it must be exactly "0"
                if j > idx and num[idx] == "0":
                    break
                part_str = num[idx:j + 1]
                part_val = int(part_str)
                if idx == 0:
                    # First number: start the expression (no operator in front)
                    dfs(j + 1, part_str, part_val, part_val)
                else:
                    # '+' : new value is cur + part; last becomes +part
                    dfs(j + 1, expr + "+" + part_str, cur + part_val, part_val)
                    # '-' : new value is cur - part; last becomes -part
                    dfs(j + 1, expr + "-" + part_str, cur - part_val, -part_val)
                    # '*' : we must respect precedence.
                    # Example: cur = (A + last), and we want (A + last * part).
                    # So remove last, then add last*part:
                    # new_cur = cur - last + (last * part)
                    dfs(j + 1, 
                    expr + "*" + part_str, 
                    cur - last + (last * part_val), 
                    last * part_val
                    )

        dfs(0, "", 0, 0)
        return res