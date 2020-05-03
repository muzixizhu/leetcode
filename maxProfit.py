# -*- coding: UTF-8 -*-
# Say you have an array prices for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.


# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 找出连续的递增序列

class Solution:
    def maxProfit_1(self, prices):
        if len(prices) <= 1:
            return 0
        p_start = p_end = 0
        profit = 0
        while p_start < len(prices):
            while p_end + 1 < len(prices) and prices[p_end + 1] >= prices[p_end]:
                p_end += 1
            if p_start <= p_end:
                profit += prices[p_end] - prices[p_start]
                p_start = p_end + 1
            else:
                profit += prices[p_end] - prices[p_start]
                return profit
        return profit
    def maxProfit(self,prices):
        maxpro = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxpro += prices[i] - prices[i - 1]

        return maxpro


def run():
    nums_1 = [7,1,5,3,6,4]
    nums_2 = [1,2,3,4,5]
    nums_3 = [7,6,4,3,1]
    solver = Solution()
    print(solver.maxProfit(nums_1))
    print(solver.maxProfit(nums_2))
    print(solver.maxProfit(nums_3))


if __name__=="__main__":
    run()



