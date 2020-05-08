class Solution:
    def maxSubArray(self, nums):
        max_so_far = nums[0]
        max_ending_here = 0

        for i in range(len(nums)):
            max_ending_here += nums[i]

            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far


class Solution_2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        maxsum = dp[0]

        for i in range(1, length):
            if dp[i - 1] + nums[i] >= nums[i]:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
            if dp[i] >= maxsum:
                maxsum = dp[i]

        return maxsum

def run():
    solver = Solution_2()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solver.maxSubArray(nums))
    assert solver.maxSubArray(nums) == 6

if __name__=='__main__':
    run()