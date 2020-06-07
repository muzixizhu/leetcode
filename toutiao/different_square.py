# 给你一个有序整数数组，数组中的数可以是正数、负数、零，请实现一个函数，这个函数返回一个整数：返回这个数组所有数的平方值中有多少种不同的取值。举例：
#
# nums = {-1,1,1,1},
#
# 那么你应该返回的是：1。因为这个数组所有数的平方取值都是1，只有一种取值
#
# nums = {-1,0,1,2,3}
#
# 你应该返回4，因为nums数组所有元素的平方值一共4种取值：1,0,4,9

class Solution:
    def countdiffsquares(self, ordered_list):
        if len(ordered_list) <= 1:
            return len(ordered_list)
        i =0
        j =len(ordered_list)-1
        res=0
        print("initial res:", res)
        while i <= j:
            num1 = abs(ordered_list[i])
            num2 = abs(ordered_list[j])
            print('step {}{}, {}{}'.format(i,j,num1,num2))
            if num1>num2:
                res += 1
                while i<=j and abs(ordered_list[i]) == num1:
                    i += 1
            elif num1<num2:
                res += 1
                while i<=j and abs(ordered_list[j] == num2):
                    j -= 1
            else:
                print('step {} {}, {} {} coming here'.format(i, j, num1, num2))
                res += 1
                print('cur res:'.format(res))
                while i<=j and abs(ordered_list[i]) == num1:
                    i += 1
                print('i = {}'.format(i))
                while i<=j and abs(ordered_list[j])==num2:
                    j -= 1
                print('j = {}'.format(j))
        return res

if __name__=="__main__":
    nums_1 = [-1,0,1,2,3]
    nums_2 = [-1, 0, 1,1,1]
    solver = Solution()
    print(solver.countdiffsquares(nums_1))
    print(solver.countdiffsquares(nums_2))





