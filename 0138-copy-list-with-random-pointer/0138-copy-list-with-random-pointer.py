"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        toCopy = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            toCopy[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = toCopy[curr]
            copy.next = toCopy[curr.next]
            copy.random = toCopy[curr.random]
            curr = curr.next
        return toCopy[head]