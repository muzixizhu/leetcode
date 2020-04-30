# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    def singleNumber(self, nums):
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

def run():
    nums= [4,1,2,1,2]
    solver = Solution()
    print(solver.singleNumber(nums))

if __name__=="__main__":
    run()
