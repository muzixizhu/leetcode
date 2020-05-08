# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_map = {}
        sum_cur = 0
        max_length = 0
        hash_map[0] = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                sum_cur += 1
            else:
                sum_cur -= 1
            if sum_cur not in hash_map:
                hash_map[sum_cur] = i
            else:
                max_length = max(i - hash_map[sum_cur], max_length)

        return max_length