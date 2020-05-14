# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return
        head_p = ListNode(0)
        head_p.next = head
        while head.next:
            tmp = head.next
            head.next = head.next.next
            tmp.next = head_p.next
            head_p.next = tmp
        return head_p.next
