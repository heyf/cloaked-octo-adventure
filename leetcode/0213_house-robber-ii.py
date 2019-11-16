#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
from typing import List

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        def helper(start, end):
            if end < start:
                return 0
            return max(nums[end]+helper(0,end-2), helper(0,end-1))
        end = len(nums) - 1
        return max(nums[end]+helper(1,end-2), helper(0,end-1))

# @lc code=end
s = Solution()
# ret = s.rob([2,3,2])
# ret = s.rob([1,2,3,1])
ret = s.rob([2,1,1,2]) #WA1: expected 3
print(ret)