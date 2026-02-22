from collections import defaultdict
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            if key not in count:
                count[key] = []
            count[key].append(s)
        return list(count.values())
