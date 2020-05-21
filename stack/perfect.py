


class Solution():
    def openclock(self, deadends, target):
        deadends = set(deadends)
        if target in deadends or '0000' in deadends: return -1
        que = collections.deque()
        que.append('0000')
        visited = set(['0000'])
        step = 0
        while que:
            step += 1
            size = len(que)
            for i in range(size):
                point = que.popleft()
                for j in range(4):
                    for k in range(-1, 2, 2):
                        newpoint = [i for i in point]
                        newpoint[i]= str((int(newpoint[i]) + k)%10)
                        newpoint = ''.join(newpoint)
                        if newpoint == target:
                            return step
                        if newpoint in visited or newpoint in deadends:
                            continue
                        que.append(newpoint)
                        visited.add(newpoint)
        return -1



