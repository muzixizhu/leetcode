# -*- coding:utf-8 -*-


def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):
    return maze[pose[0]][pose[1]] == 0


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        return True
    for i in range(4):
        nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                return True
    return False


# stack Solution
# 栈与回溯法

class mase_Stack():
    def stack_recur(self, maze, start, end):
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        mark(start, end)
        if start == end:
            return True
        stack = []
        for i in range(4):
            nextp = (start[0] + dirs[i][0], start[1] + dirs[i][1])
            if passable(maze, nextp):
                stack.append((start, i))
        while len(stack) >0:
            pos, i = stack.pop()
            cur_pos = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            mark(maze, cur_pos)
            if cur_pos == end:
                return True
            for i in range(4):
                next_step = (cur_pos[0] + dirs[i][0], cur_pos[1] + dirs[i][1])
                if passable(maze, next_step):
                    stack.append((cur_pos, i))

        return False

# 书中实现

def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    stack = []
    mark(maze, start)
    stack.append((start, 0))
    while len(stack)>0:
        pos, nxt = stack.pop()
        for i in range(nxt, 4):
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            if nextp == end:
                print_path(end, pos, stack)
                return
            if passable(maze, nextp):
                stack.append((pos, i+1))
                mark(maze, nextp)
                stack.append((nextp, 0))
                break
    print("No path found.")

# 这种方式更好，能够更清晰的记录没有探索的入口以及已经探索过的

def maze_solver_queue(maze, start, end):
    mark(maze, start)
    if start == end:
        print(start)
        return
    que = collections.deque()
    que.enqueue(start)
    while not que.is_empty():
        pos = que.dequeue()
        for i in range(4):
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            if passable(maze, nextp):
                if nextp == end:
                    print('path found')
                    return
                deque.enqueue(nextp)
                mark(maze, nextp)
    return False



