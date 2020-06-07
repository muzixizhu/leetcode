class Solution():
    def max_profit(self, nums):
        cur_min= nums[0]
        max_profit = nums[0] - cur_min
        for i in range(1, len(nums)):
            cur_min = min(cur_min, nums[i])
            max_profit = max(nums[i] - cur_min, max_profit)
        return max_profit


if __name__=="__main__":
    nums_1 = [7,1,5,3,6,4]
    solver = Solution()
    print(solver.max_profit(nums_1))