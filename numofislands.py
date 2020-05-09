#   Number of Islands
# Solution
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
import collections
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    self.dfs(grid, r, c)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[i][j] = 0
        for dir in dirs:
            nr, nc = i + dir[0], j + dir[1]
            if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                if grid[nr][nc] == 1:
                    self.dfs(grid, nr, nc)

# class Solution_2():
#     def numOfIslands(self, grid):
#         if not grid or not grid[0]: return 0
#
#         M, N = len(grid), len(grid[0])
#         res = 0
#         dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#         que = collections.deque()
#         for i in range(M):
#             for j in range(N):
#                 if grid[i][j] == 1:
#                     res += 1
#                     grid[i][j] = 0
#                     que.append((i, j))
#                     while que:
#                         x, y = que.pop()
#                         for dir in dirs:
#                             nx, ny = x+dir[0], y+dir[1]
#                             if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 1:
#                                 grid[nx][ny] = 0
#                                 que.append((nx,ny))
#         return res

class Solution_2(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        que = collections.deque()
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        print('coming here')
        for i in range(M):
            for j in range(N):
                print(grid[i][j])
                if grid[i][j] == 1:
                    print('find flag')
                    res += 1
                    grid[i][j] = 0
                    que.append((i, j))
                    while que:
                        x, y = que.pop()
                        for d in directions:
                            nx, ny = x + d[0], y + d[1]
                            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 1:
                                grid[nx][ny] = 0
                                que.append((nx, ny))
        return res

def run():
    grid = [[1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]]
    # solver = Solution()
    # print('sol 1:', solver.numIslands(grid))
    solver_2 = Solution_2()
    print('output2:', solver_2.numIslands(grid))


if __name__=="__main__":
    run()
