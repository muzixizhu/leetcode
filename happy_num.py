# Write an algorithm to determine if a number n is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer,
# replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
# Return True if n is a happy number, and False if not.


class Solution():
    def is_happy(self, num):
        cycle_set = set()
        while True:
            squre_sum = sum(int(i) * int(i) for i in str(num))
            if squre_sum == 1:
                return True
            elif squre_sum not in cycle_set:
                cycle_set.add(squre_sum)
            else:
                return False
            num = squre_sum

def run():
    solver = Solution()
    print(solver.is_happy(19))

    print('11 is happy number?', solver.is_happy(11))
if __name__=="__main__":
    run()



