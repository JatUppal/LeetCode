# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prevA = list1
        for _ in range(a-1):
            prevA = prevA.next
        afterB = prevA
        for _ in range(b - a + 2):
            afterB = afterB.next
        prevA.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = afterB
        return list1
        
        