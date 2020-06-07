The idea is to recusively explore allpossible paths from the starting

cell '1', stopping exploration as soon as paths are
found to be invalid.The trick to ensure each cell is traversed only once is to change
its value from '0' to '-1' right after its visited, so it is considered a wall.However, after
checking valid movements in all 4 directions, be careful
to revert grid values to 0 in order to consider previously unexplored paths( if not, grid will only be traversed once).

First, we loop
through all
elements of
grid to(1)
count all
traversable cells(i.e.
1, 2 and 0 s) and (2)
find the starting
point(i.e.cell '1' coordinates).This
information is stored in to_visit and start_r, start_crespectively.

Next, we implement
the dfs function, which will
construct
the
graph
of
all
possible
paths, backtracking
whenever
we
either(1)
find
a
wall or a
previously
visited
cell or (2)
reach
the
ending
cell
'2'
without
having
visited
all
the
grid
's 0s.


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        self.directions = (0, 1), (0, -1), (1, 0), (-1, 0)
        to_visit = 0
        for r in range(self.R):
            for c in range(self.C):
                # count all 0s, 1 and 2 cells to be visited
                if grid[r][c] != -1: to_visit += 1
                # find starting point i.e. cell 1
            if grid[r][c] == 1: start_r, start_c = r, c

        return self.dfs(grid, start_r, start_c, to_visit)

    def dfs(self, grid, r, c, to_visit):
        # check if out of range or wall found
        if not (0 <= r < self.R and 0 <= c < self.C) or grid[r][c] == -1: return 0

        # found end cell, valid path if all 0s visited
        if grid[r][c] == 2:
            return to_visit == 1

        # valid movement, keep going
        elif grid[r][c] in [0, 1]:
            res = 0
            # mark as visited
            grid[r][c] = -1
            # check movements in all 4 directions
            for dr, dc in self.directions:
                res += self.dfs(grid, r + dr, c + dc, to_visit - 1)
            # mark prev explored cell as unvisited
            grid[r][c] = 0
        return res