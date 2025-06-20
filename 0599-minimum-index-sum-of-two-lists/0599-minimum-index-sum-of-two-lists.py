class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = {}
        dict1 = {val: index for index, val in enumerate(list1)}
        for i in range(len(list2)):
            if list2[i] in dict1.keys():
                sums = i + dict1[list2[i]]
                if sums not in res:
                    res[sums] = []
                res[sums].append(list2[i])
        return res[min(res.keys())]