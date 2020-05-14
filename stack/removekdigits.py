# Remove K Digits
# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
#
# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

class Solution():
    def removeKdigits(self, nums, k):
        """
        :param nums:  str of number
        :return:
        """
        if len(nums)<=k:
            return '0'
        stack = []
        for n in nums:
            while stack and k and int(stack[-1])>int(n):
                stack.pop()
                k -= 1
            stack.append(n)
        while k:
            stack.pop()
            k -= 1
        return str(int(''.join(stack)))


if __name__=='__main__':
    nums = '1432219'
    k = 3
    solver = Solution()
    print(solver.removeKdigits(nums, k))