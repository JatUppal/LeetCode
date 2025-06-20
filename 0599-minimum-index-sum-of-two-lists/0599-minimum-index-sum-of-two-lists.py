class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = {}
        for i in range(len(list2)):
            if list2[i] in list1:
                sums = i + list1.index(list2[i])
                if sums not in res:
                    res[sums] = []
                res[sums].append(list2[i])
        return res[min(res.keys())]