# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy  # 上一组的尾节点

        while True:
            # 找到这一组的第 k 个节点
            kth = self.getKth(prev_group, k)
            if not kth:
                break
            
            group_start = prev_group.next  # 这一组的头
            next_group = kth.next          # 下一组的头

            # 断开这一组
            kth.next = None
            # 反转这一组
            prev_group.next = self.reverseList(group_start)
            # 反转后 group_start 变成了尾节点，接上下一组
            group_start.next = next_group
            # 移动到下一组
            prev_group = group_start

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev