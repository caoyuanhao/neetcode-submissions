# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curra=headA
        m={}
        while curra:
            if curra not in m:
                m[curra]=[]
            curra=curra.next
        currb=headB
        while currb:
            if currb in m:
                return currb
            currb=currb.next
        return None