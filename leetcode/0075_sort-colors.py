#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

from typing import List

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, blue = 0, len(nums) - 1
        idx = 0
        while idx <= blue:
            if nums[idx] == 0:
                nums[idx], nums[red] = nums[red], nums[idx]
                red += 1
            elif nums[idx] == 2:
                nums[idx], nums[blue] = nums[blue], nums[idx]
                idx -= 1
                blue -= 1
            idx += 1
        return
        
# @lc code=end
s = Solution()
# a = [2,0,2,1,1,0]
a = [2,0,1] # WA1
s.sortColors(a)
print(a)
