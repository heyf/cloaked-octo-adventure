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
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return right

# @lc code=end
s = Solution()
a = [1,2,1,3,5,6,4]
print(s.findPeakElement(a))
