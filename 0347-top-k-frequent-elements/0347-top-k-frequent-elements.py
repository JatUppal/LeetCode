class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        for i in range(len(freq) - 1, 0, -1):
            j = 0
            while k > 0 and j < len(freq[i]):
                res.append(freq[i][j])
                k -= 1
                j += 1
        return res
