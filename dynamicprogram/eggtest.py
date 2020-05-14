

class Solution():
    def superEggDrop(self, K, N):
        memo = {}
        def dp(K, N):
            if N == 0: return 0
            if K == 1: return N

            if (K,N) in memo:
                return memo[(K,N)]
            res = float('int')
            for i in range(1, N+1):
                res = min(res, max(dp[K-1][i-1], dp[K][N-i]) + 1)
            memo[(K, N)] = res
            return res
        return dp[(K,N)]
