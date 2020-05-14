# -*- coding:  utf-8 -*-

# 最长公共子序列（Longest Common Subsequence，简称 LCS）
# 是一道非常经典的面试题目，因为它的解法是典型的二维动态规划，
# 大部分比较困难的字符串问题都和这个问题一个套路，比如说编辑距离。
# 而且，这个算法稍加改造就可以用于解决其他问题，所以说 LCS 算法是值得掌握的。

# 输入: str1 = "abcde", str2 = "ace"
# 输出: 3
# 解释: 最长公共子序列是 "ace"，它的长度是 3

class Solution():
    def longestcommonsub(self, str1, str2):
        # dp[i][j] 定义为 我们暂时认为索引是从 1 开始的
        # ，待会的代码中只要稍作调整即可。其中，dp[i][j] 的含义是：
        # 对于 s1[1..i] 和 s2[1..j]，它们的 LCS 长度是 dp[i][j]
        # def dp(i, j):
        #     if i == 0 or j == 0:
        #         return 0
        #     elif str1[i] == str2[j]:
        #         return dp[i-1][j-1] + 1
        #     else:
        #         return max(dp[i-1][j], dp[i][j-1])
        # return dp(len(str1) -1, len(str2) -1)
        # 添加memory table
        m = len(str1)
        n = len(str2)
        dp = [[0] * (n+1)] * (m + 1)
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

if __name__=='__main__':
    str1 = 'babcde'
    str2 = 'ace'
    solver = Solution()
    print(solver.longestcommonsub(str1, str2))

