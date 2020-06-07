# Perfect Squares
# Solution
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution():
    def numSquares(self, n):
        q = [(n, 0)]
        visited = [False for _ in range(n+1)]
        visited[n] = True

        while any(q):
            num, step = q.pop()
            i = 1
            Num = num - i * i
            while Num >= 0:
                if Num == 0:
                    return step + 1
                if not visited[Num]:
                    q.append((Num, step+1))
                    visited[Num] = True
                i += 1
                Num = num - i**2


if __name__=="__main__":
    n = 7
    solver = Solution()
    print(solver.numSquares(n))
