# -*- coding: UTF-8 -*-
# """
# Ugly Numbers
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, …
# shows the first 11 ugly numbers. By convention, 1 is included.
# Given a number n, the task is to find n’th Ugly number.
# Input  : n = 7
# Output : 8
# Input  : n = 10
# Output : 12
# Input  : n = 15
# Output : 24
# Input  : n = 150
# Output : 5832
# """


class Solution():
    def is_ugly_num(self, num):
        while num % 5 == 0:
            print('congurence 5')
            num /= 5
        while num % 3 == 0:
            print('congurence 3')
            num /= 3
        while num % 2 == 0:
            print('congurence 2')
            num /= 2
        return num == 1

    def ugly_num(self, n):
        cnt = 1
        init = 1
        while cnt < n:
            init += 1
            if self.is_ugly_num(init):
                print('{} is the {} th ugly number'.format(init, cnt))
                cnt += 1

        return init - 1


def run():
    solver = Solution()
    print(solver.ugly_num(7))
    print(solver.ugly_num(10))
    print(solver.ugly_num(15))
    print(solver.ugly_num(150))


if __name__=="__main__":
    run()

