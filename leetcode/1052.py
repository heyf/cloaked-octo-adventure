# Grumpy Bookstore Owner - LeetCode Contest
# https://leetcode.com/contest/weekly-contest-138/problems/grumpy-bookstore-owner/

class Solution:
    def maxSatisfied(self, customers, grumpy, X: int) -> int:
        satisfied_by_default = customers[0] * (1 - grumpy[0])
        max_by_trick = customers[0] * grumpy[0]
        grumpy_sum = customers[0] * grumpy[0]
        for i in range(1,len(customers)):
            satisfied_by_default += customers[i] * (1 - grumpy[i])
            grumpy_sum += customers[i] * grumpy[i]
            if i >= X:
                grumpy_sum -= customers[i-X] * grumpy[i-X]
            max_by_trick = max(grumpy_sum, max_by_trick)
        return satisfied_by_default + max_by_trick

s = Solution()
# print(s.maxSatisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3))
print(s.maxSatisfied([9,10,4,5],[1,0,1,1],1))
