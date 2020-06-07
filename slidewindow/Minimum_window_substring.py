import collections

class Solution():
    def minimum_window_substr(self, S, T):
        """find minimum window in S Contain T"""
        need_win = {}
        for i in T:
            need_win[i] += 1 if i in need_win else need_win[i]=1
        slide_win = {}
        left , right = 0, 0
        valid = 0
        start = 0
        window_len = len(S) + 1
        while right<len(S):
            char = S[right]
            right += 1
            if char in need_win:
                slide_win[char] += 1 if char in slide_win else slide_win[char] = 1
                if slide_win[char] == need_win[char]:
                    valid += 1

            while valid == len(need_win):
                if right - left < window_len:
                    start = left
                    window_len = right - left
                drop_char = S[left]
                left += 1

                if drop_char in need_win:
                    if slide_win[drop_char] == need_win[drop_char]:
                        valid -= 1
                    slide_win[drop_char] -= 1
            slide_win[S[right]] += 1
        return S[start:start+window_len] if window_len<len(S)+1 else ""


if __name__=="__main__":
    S = 'ebbancf'
    T = 'abc'
    solver = Solution()
    print(solver.minimum_window_substr(S, T))