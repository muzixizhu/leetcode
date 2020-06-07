import collections

class Solution():
    def sort_by_freq(self, s):
        freq_dict = collections.defaultdict(int)
        for i in s:
            freq_dict[i] += 1
        res = ''
        while len(freq_dict):
            m = max(freq_dict, key=freq_dict.get)
            print(m,freq_dict[m])
            res += m*freq_dict[m] 
            del freq_dict[m]
        return res


if __name__=="__main__":
    s = 'tree'
    solver = Solution()
    print(solver.sort_by_freq(s))