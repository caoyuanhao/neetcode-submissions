# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(0)
        curr=res
        h=0
        while l1 or l2 or h:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            s=v1+v2+h
            curr.next=ListNode(s%10)
            
            if s>=10:
                h=1
            else:
                h=0
            if l1:l1=l1.next
            if l2:l2=l2.next
            curr=curr.next
        return res.next