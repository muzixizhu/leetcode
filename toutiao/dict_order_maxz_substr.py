# 给一个字符串得到它字典序最大的子序列。（他的表述方式是，删除一些字符，
# 使得剩下的字符构成的字符串字典序是最大的）

class Solution():
    def biggest_substr(self, s):
        stack = []
        for i in range(len(s)):
            while stack and stack[-1]<s[i]:
                stack.pop()
            stack.append(s[i])
        return ''.join(stack)
    def sol_2(self, s):
        res = s[-1]
        for i in range(len(s)-2,-1,-1):
            if s[i]>=res[0]:
                res = s[i] + res
        return res


if __name__=='__main__':
    s='abcbabcba'
    solver = Solution()
    print(solver.biggest_substr(s))
    print(solver.sol_2(s))

