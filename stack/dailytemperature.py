
Daily Temperatures
Solution
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].


class Solution():
    def dailyTemperature(self, T):
        ans = [0]*len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                cur_ind = stack.pop()
                ans[cur_ind] = i - cur_ind
            stack.append(i)
        return ans


if __name__ =="__main__":
    test_list = [73, 74, 75, 71, 69, 72, 76, 73]
    solver = Solution()
    print(solver.dailyTemperature(test_list))