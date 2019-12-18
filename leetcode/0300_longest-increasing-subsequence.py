#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

from typing import List

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = dict()
        res = min(1, len(nums))
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                res = max(res, dp[i])
        return res

# @lc code=end
s = Solution()
# nums = [10,9,2,5,3,7,101,18] # 4
# WA1:
# nums = [0] # 1
# nums = [2,1]
# WA2:
nums = []
ret = s.lengthOfLIS(nums)
print(ret)