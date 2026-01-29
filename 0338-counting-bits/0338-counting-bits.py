class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans[i] will store the number of 1s in the binary form of i
        ans = [0] * (n + 1)

        # Start from 1 since ans[0] = 0 is already correct
        for i in range(1, n + 1):
            # i // 2 removes the last bit (right shift)
            # i % 2 tells us if the last bit is 1 or 0
            ans[i] = ans[i // 2] + (i % 2)

        return ans