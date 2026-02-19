class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        result = []
        for i in range(len(freq) - 1, 0, -1):
            if not freq[i]:
                continue
            j = 0
            while k > 0 and j < len(freq[i]):
                result.append(freq[i][j])
                k -= 1
                j += 1
        return result