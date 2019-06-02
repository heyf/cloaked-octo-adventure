# 1043. Partition Array for Maximum Sum - LeetCode Contest
# https://leetcode.com/contest/weekly-contest-136/problems/partition-array-for-maximum-sum/

# Runtime: 1784 ms
# Memory Usage: 97.4 MB

from functools import lru_cache

INT_MIN = 0

class Solution:
    @lru_cache(maxsize=None)
    def subarray_maxsum(self,start,end):
        return max(self.A[start:end]) * (end - start)

    @lru_cache(maxsize=None)
    def msa_helper(self,start,end):
        if end > len(self.A):
            end = len(self.A)
        if self.K >= end - start:
            return max(self.A[start:end]) * (end - start)
        current_max = INT_MIN
        for i in range(start+1, start+self.K+1, 1):
            current_max = max(current_max,self.subarray_maxsum(start,i)+self.msa_helper(i,end))
        return current_max
    
    def maxSumAfterPartitioning(self, A, K) -> int:
        self.A = A
        self.K = K
        return self.msa_helper(0,len(A))

# 数组边界的思考方式
    
ans = [
    {"A": [1,15,7,9,2,5,10], "K": 3, "Output": 84},
    {"A": [9,15,7,1,2,10], "K": 3, "Output": 75},
    {"A": [1], "K": 100, "Output": 1}
]

for i in ans:
    s = Solution()
    r = s.maxSumAfterPartitioning(i["A"],i["K"])
    print(r, r == i["Output"])