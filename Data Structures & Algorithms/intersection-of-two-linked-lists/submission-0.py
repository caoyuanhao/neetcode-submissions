# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curra=headA
        
        while curra:
            currb=headB
            while currb:
                if currb!=curra:
                    currb=currb.next
                else:
                    return currb
            curra=curra.next
        return None