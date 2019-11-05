#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

from typing import List

# @lc code=start
INT_MIN = - 2 ** 64 + 1

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.insert(0, INT_MIN)
        nums.append(INT_MIN)
        for i in range(len(nums)):
            if nums[i+1] > nums[i] and nums[i+1] > nums[i+2]: 
                return i
        return -1

# @lc code=end
s = Solution()
a = [1,2,1,3,5,6,4]
print(s.findPeakElement(a))
