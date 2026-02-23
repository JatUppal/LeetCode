# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        # [3,4, 2, 7]
        # [4, 6, 5]
        res = []
        carry = 0
        while stack1 and stack2:
            num1 = stack1.pop()
            num2 = stack2.pop()
            total = num1 + num2
            if carry == 1:
                total += 1
                carry = 0
            if total >= 10:
                total = total % 10
                carry = 1
            res.append(total)
        remain = stack1 if stack1 else stack2
        while remain:
            value = remain.pop()
            if carry == 1:
                value += 1
                carry = 0
            if value >= 10:
                value = value % 10
                carry = 1
            res.append(value)
        if carry == 1:
            res.append(carry)
        dummy = ListNode()
        curr = dummy
        for i in range(len(res) - 1, -1, -1):
            curr.next = ListNode(res[i])
            curr = curr.next
        return dummy.next            