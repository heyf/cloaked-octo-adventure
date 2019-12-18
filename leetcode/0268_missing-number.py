#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

from typing import List

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= (i+1) ^ nums[i]
        return res

# @lc code=end
s = Solution()
nums = [2,0,1]
ret = s.missingNumber(nums)
print(ret)