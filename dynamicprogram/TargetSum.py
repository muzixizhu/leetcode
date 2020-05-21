# Target Sum
# Solution
# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        # _len = len(nums)
        # dp = [collections.defaultdict(int) for _ in range(_len + 1)]
        # dp[0][0] = 1
        # for i, num in enumerate(nums):
        #     for sum, cnt in dp[i].items():
        #         dp[i + 1][sum + num] += cnt
        #         dp[i + 1][sum - num] += cnt
        # return dp[_len][S]

        _len = len(nums)
        dp = [collections.defaultdict(int) for _ in range(_len + 1)]
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for sum,cnt in dp[i].items:
                dp[i+1][sum + num] += cnt
                dp[i+1][sum - num] += cnt
        return dp[_len][S]
