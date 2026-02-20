# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = head
        curr = head
        res = 0
        n = -1
        while temp:
            n += 1
            temp = temp.next
        while curr:
            if curr.val == 1:
                res += 2 ** n
            curr = curr.next
            n -= 1
        return res
        