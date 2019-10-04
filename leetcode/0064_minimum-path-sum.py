#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

from typing import List

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        dp = []
        for i, v in enumerate(grid[0]):
            if i == 0:
                dp.append(v)
            else:
                dp.append(v+dp[-1])
        for row in grid[1:]:
            for i, v in enumerate(row):
                if i == 0:
                    dp[i] += v
                else:
                    dp[i] = min(dp[i-1],dp[i]) + v
        return dp[-1]

# @lc code=end
s = Solution()
ret = s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])
print(ret)
