# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node):
            if not node:
                return -1
            h = 1 + max(dfs(node.left), dfs(node.right))
            if len(res) == h:
                res.append([])
            res[h].append(node.val)
            return h
        dfs(root)
        return res