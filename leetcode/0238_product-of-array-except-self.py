#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

from typing import List

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        for idx in range(1,len(nums)):
            output.append(output[-1]*nums[idx-1])
        backward = 1
        for idx in range(len(nums)-1, -1,-1):
            output[idx] *= backward
            backward *= nums[idx]
        return output

# @lc code=end
s = Solution()
ret = s.productExceptSelf([1,2,3,4])
print(ret)