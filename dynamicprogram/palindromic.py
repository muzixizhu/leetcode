


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # d = [[False] * len(s)] * len(s)
        # ans = ''
        # for i in range(len(s)):
        #     d[i][i] = True
        #     ans = s[-1]
        # maxlen = 1
        # for start in range(len(s) - 1, -1, -1):
        #     for end in range(start + 1, len(s)):
        #         if s[start] == s[end]:
        #             if end - start == 1 or d[start+1][end-1]:
        #                 d[start][end] == True
        #             if maxlen<end -start + 1:
        #                 maxlen = end-start+1
        #                 ans = s[start:end+1]
        # return ans

        n = len(s)
        # Form a bottom-up dp 2d array
        # dp[i][j] will be 'true' if the string from index i to j is a palindrome.
        dp = [[False] * n  for _ in range(n)]

        ans = ''
        # every string with one character is a palindrome
        for i in range(n):
            dp[i][i] = True
            ans = s[i]

        maxLen = 1
        for start in range( n -1, -1, -1):
            for end in range(star t +1, n):
                # palindrome condition
                if s[start] == s[end]:
                    # if it's a two char. string or if the remaining string is a palindrome too
                    if end - start == 1 or dp[star t +1][en d -1]:
                        # 上面的状态转移决定了循环的方向
                        dp[start][end] = True
                        if maxLen < end - start + 1:
                            maxLen = end - start + 1
                            ans = s[start: end+1]

        return ans

