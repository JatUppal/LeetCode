"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        prev = head
        curr = head.next
        while True:
            if prev.val <= insertVal <= curr.val:
                break
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    break
            prev = curr
            curr = curr.next
            if prev == head:
                break
        prev.next = Node(insertVal, curr)
        return head
        