from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        result = []
        for key, count in counts.most_common(k):
                result.append(key)
        return result
