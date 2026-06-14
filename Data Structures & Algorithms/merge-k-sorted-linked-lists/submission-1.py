# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists)>1:
            merged=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                merged.append(self.mergeTwoLists(l1,l2))
            lists=merged
        return lists[0]


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0)
        res=head
        while list1 and list2:
            if list1.val<list2.val:
                head.next=list1
                list1=list1.next
                head=head.next
            else:
                head.next=list2
                list2=list2.next
                head=head.next                
        if list1:
            head.next=list1
        if list2:
            head.next=list2
        return res.next