#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
from typing import List

# @lc code=start
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        @lru_cache(maxsize=None)
        def helper(start, end):
            if end < start:
                return 0
            return max(nums[end]+helper(start,end-2), helper(start,end-1))
        end = len(nums) - 1
        return max(nums[end]+helper(1,end-2), helper(0,end-1))

# @lc code=end
s = Solution()
# ret = s.rob([2,3,2])
# ret = s.rob([1,2,3,1])
# ret = s.rob([2,1,1,2]) # WA1: expected 3
ret = s.rob([
    94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 
    61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 
    61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 
    57, 86, 81, 72]) # TLE
print(ret)