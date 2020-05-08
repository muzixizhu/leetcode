class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        for s in magazine:
            if s not in mag_dict:
                mag_dict[s] = 1
            else:
                mag_dict[s] += 1
        print(mag_dict)
        for t in ransomNote:
            print('current char is {}'.format(t))
            if t not in mag_dict:
                print('t not in mag_dict')
                return False
            elif mag_dict[t] <= 0:
                print("{} {}".format(t, mag_dict))
                return False
            else:
                mag_dict[t] -= 1
                print('de ', mag_dict)
        return True

def run():
    t = 'aa'
    s = 'ab'
    solver = Solution()
    print(solver.canConstruct(t, s))

if __name__=="__main__":
    run()