class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need_win = {}
        if len(s2)<len(s1):return False
        for char in s1:
            if char not in need_win:
                need_win[char] = 1
            else:
                need_win[char] += 1
        print(need_win)
        slid_win = {}
        for i in range(0,len(s2)):
            if i>=len(s1):
                print('i ={}'.format(i))
                slid_win[s2[i-len(s1)]] -= 1
                if slid_win[s2[i-len(s1)]] == 0:
                    slid_win.pop(s2[i-len(s1)])
            if s2[i] not in slid_win:
                slid_win[s2[i]] = 1
            else:
                slid_win[s2[i]] += 1
            print('i: {}, slid_win:{}'.format(i, slid_win))
            if need_win == slid_win:
                return True
        return False

if __name__=="__main__":
    s1 = 'ab'
    s2 = "eidbaooo"
    solver = Solution()
    print(solver.checkInclusion(s1, s2))