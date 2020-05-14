class Solution():
    def package(self, weights, values, W, N):
        # if len(weights) != len(values): return
        # memo = {}
        # def dp(w,n):
        #     if str(w) +' '+ str(n) in memo: return memo[str(w) + ' ' + str('n')]
        #     if w == 0:
        #         return 0
        #     if n == 0:
        #         return 0
        #     if w < 0: return -1
        #     if n < 0: return -1
        #     res = float('-inf')
        #     for i in range(len(weights)):
        #         subproblem = dp(w - weights[i], n-1)
        #         if subproblem == -1: continue
        #         res = max(res, values[i] + subproblem)
        #     memo[str(w) + ' ' + str('n')] = res if res != float('-inf') else -1
        #     return memo[str(w) + ' ' + str('n')]
        # return dp(W,N)
        dp = [[0] * (W + 1)] * (N+1)
        print(dp)
        for i in range(1, N+1):
            for j in range(1, W+1):
                if j - weights[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j - weights[i-1]] + values[i-1])
        return dp[N][W]


if __name__=="__main__":
    W = 4
    N = 3
    weights = [2, 1, 3]
    values = [4, 2, 3]
    solver = Solution()
    print(solver.package(weights, values, W, N))