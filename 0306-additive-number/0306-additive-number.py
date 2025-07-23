class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                num1, num2 = num[:i], num[i:j]
                if (len(num1) > 1 and num1[0] == "0") or (len(num2) > 1 and num2[0] == "0"):
                    continue
                k = j
                while k < n:
                    result = str(int(num1) + int(num2))
                    if not num.startswith(result, k):
                        break
                    k += len(result)
                    num1, num2 = num2, result
                if k == n:
                    return True
        return False
