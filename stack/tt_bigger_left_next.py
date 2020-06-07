

class Solution():
    def bigger_left(self, nums):
        stack = []
        new_list = nums[::-1]
        print('nums:', nums)
        print('nes_list:', new_list)
        res = [0] * len(nums)
        for i in range(len(nums)):
            while stack and new_list[stack[-1]] < new_list[i]:
                temp = stack.pop()
                res[temp] = new_list[i]
            stack.append(i)
        return res[::-1]


if __name__ =="__main__":
    test_list = [73, 74, 75, 71, 69, 72, 76, 73]
    solver = Solution()
    print(solver.bigger_left(test_list))