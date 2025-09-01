# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next
        prev2 = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev2
            prev2 = curr
            curr = temp
        tail = prev.next
        prev.next = prev2
        tail.next = curr
        
        return dummy.next