

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p_stat = p_dummy = ListNode(0)
        # p_dummy.next = head
        p_head = head
        while p_head:
            print('cur p_head', p_head.val)
            while p_head and p_head.val == val:
                print('doing this')
                p_head = p_head.next
            # print('now p_head', p_head.val)
            if p_head is not None:
                p_dummy.next = p_head
                p_dummy = p_dummy.next
                print('cur p_dummy', p_dummy.val)
                p_head = p_head.next
            else:
                p_dummy.next = None
        return p_stat.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_1:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p_stat = p_dummy = ListNode(0)
        p_head = head
        while p_head:
            while p_head and p_head.val == val:
                p_head = p_head.next
            if p_head is not None:
                p_dummy.next = p_head
                p_dummy = p_dummy.next
                p_head = p_head.next
            else:
                p_dummy.next = None
        return p_stat.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(6)

if __name__=='__main__':
    solver = Solution()
    p_head = solver.removeElements(head,6)
    while p_head:
        print(p_head.val)
        p_head = p_head.next