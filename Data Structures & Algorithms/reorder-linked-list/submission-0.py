# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1=head
        p2=head
        while p1 and p2 and p2.next:
            p1=p1.next
            p2=p2.next.next
        if p1:
            p2=p1.next
            p1.next=None
        curr=p2
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        h=head
        while h and prev:
            temp1=h.next
            temp2=prev.next
            h.next=prev
            prev.next=temp1
            h=temp1
            prev=temp2
        

