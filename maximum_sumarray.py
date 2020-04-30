# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_ending_here = 0

        for i in range(len(nums)):
            max_ending_here += nums[i]

            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

def run():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solver = Solution()
    print(solver.maxSubArray(nums))

if __name__=="__main__":
    run()