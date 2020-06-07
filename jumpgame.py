# -*- coding: utf-8 -*-
# Constraints:
#
# 1 <= nums.length <= 3 * 10 ^ 4
# 0 <= nums[i][j] <= 10 ^ 5
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.



class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1#默认向前走一步，即从i走到i+1,剩余步数减1
                step = max(step, nums[i])#将此位置步数与step作比较，最大值当做step
            else:
                return False
        return True