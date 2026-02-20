class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        freq = [[] for i in range(len(nums) + 1)]
        for n in count.keys():
            freq[count[n]].append(n)
        for i in range(len(freq) - 1, -1, -1):
            for val in freq[i]:
                if k == 0:
                    return res
                res.append(val)
                k -= 1
        return res