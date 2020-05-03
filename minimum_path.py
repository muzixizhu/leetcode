# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j>0:
                    grid[i][j] += grid[i][j-1]
                elif i>0 and j == 0:
                    grid[i][j] += grid[i-1][j]
                elif i>0 and j>0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[rows-1][cols-1]

    