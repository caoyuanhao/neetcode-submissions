# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        h=prev
        new_head = h

        if n==1 and h:
            new_head=h.next
            h.next=None
        elif n==2 and h and h.next:
            temp=h.next.next
            h.next.next=None
            h.next=temp
        elif n>2:
            while h and n>2:
                h=h.next
                n-=1
            if h and h.next:
                temp=h.next.next
                h.next.next=None
                h.next=temp
        p=None
        c = new_head
        while c:
            temp=c.next
            c.next=p
            p=c
            c=temp
        return p