class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if (i != j and (n + m) == target):
                    result.append(i)
        return result
        