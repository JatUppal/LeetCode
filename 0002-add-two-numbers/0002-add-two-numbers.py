# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Understand - Inputs: 2 linked lists, Output, 1 single linked list. contraints each range [1,100]
# each node value between 0 and 9
# Implement - dummy Node, temp to dummy
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            digit = total % 10
            carry = total // 10
            temp.next = ListNode(digit)
            temp = temp.next
        return dummy.next
