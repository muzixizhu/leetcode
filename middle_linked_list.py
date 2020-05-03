class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p_1 = p_2 = head
        while p_2 and p_2.next :
            p_1 = p_1.next
            p_2 = p_2.next.next
        return p_1


class Solution_1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        temp = 1
        for i in range(len(nums)):
            res.append(temp)
            temp = temp * nums[i]
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * temp
            temp = temp * nums[i]
        return res