# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution():
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        p_0 = 0
        while p_0 < len(nums):
            while nums[p_0] != 0:
                p_0 += 1
            p_none_0 = p_0
            while p_none_0 < len(nums) and nums[p_none_0] == 0:
                p_none_0 += 1
            if p_none_0 < len(nums):
                nums[p_0], nums[p_none_0] = nums[p_none_0], nums[p_0]
            else:
                return nums
            p_0 = p_0 + 1
        return nums

def run():
    input = [0,1,0,3,12]
    solver = Solution()
    print(input)
    print(solver.moveZeroes(input))


if __name__=="__main__":
    run()
