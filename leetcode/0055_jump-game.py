#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
'''
Your runtime beats 65.32 % of python3 submissions
Your memory usage beats 7.14 % of python3 submissions (16 MB)
'''

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if i > reach or reach >= len(nums) - 1:
                break
            else:
                reach = max(reach, i+nums[i])
        return reach >= len(nums) - 1

