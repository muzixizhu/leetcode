# Linked List Cycle
# Solution
# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos
# which represents the position (0-indexed) in the linked list where
# tail connects to. If pos is -1, then there is no cycle in the linked
# list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p_slow = head
        p_fast = head
        while p_fast and p_fast.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
            if p_slow != p_fast:
                continue
            else:
                return True
        return False