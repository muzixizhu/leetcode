
class Solution():
    def rotateRight(self, head, k):
        if not head or k ==0:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        cnt = 0
        while p.next:
            p = p.next
            cnt += 1
        p.next = dummy.next
        step = cnt - (k % cnt)
        for i in range(0, step):
            p = p.next
        head = p.next
        p.next = None
        return head
