# class Solution:
#     def subarraySum(self, nums, k):
#         cnt = 0
#         sum_hash = {}
#         sum_cur = 0
#         for i in range(len(nums)):
#             sum_cur += nums[i]
#             print('sum_cur now,', sum_cur)
#             if sum_cur not in sum_hash:
#                 sum_hash[sum_cur] = 1
#             else:
#                 sum_hash[sum_cur] += 1
#         print('hash table completed')
#         print(sum_hash)
#         values = sum_hash.keys()
#         print('values:', values)
#         for i in values:
#             for j in values:
#                 if abs(i - j) == k:
#                     cnt += sum_hash[i] * sum_hash[j]
#         return cnt//2 + sum_hash[k]

import collections


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = collections.defaultdict(int)
        d[0] = 1
        sum = 0
        res = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in d:
                res += d[sum - k]
            d[sum] += 1
        return res


def run():
    exp = [-1,-1,1]
    solver = Solution()
    print(solver.subarraySum(exp, 0))

if __name__=="__main__":
    run()