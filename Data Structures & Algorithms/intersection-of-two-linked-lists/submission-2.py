# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curra=headA
        currb=headB
        while curra!=currb:
            curra=curra.next if curra else headB
            currb=currb.next if currb else headA
        return currb
