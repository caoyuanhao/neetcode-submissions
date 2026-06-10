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
        if not head:
            return None
        maps={}
        h=head
        while h:
            maps[h]=Node(h.val)
            h=h.next
        h=head
        while h:
            if h.next:
                maps[h].next=maps[h.next]
            if h.random:
                maps[h].random=maps[h.random]
            h=h.next
        return maps[head]
