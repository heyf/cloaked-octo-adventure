#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
from typing import List

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        dp = []
        flag = 1
        for i, v in enumerate(obstacleGrid[0]):
            if v == 1:
                flag = 0
            dp.append(flag)
        for row in obstacleGrid[1:]:
            for i, v in enumerate(row):
                if v == 0:
                    dp[i] = 1 if i == 0 else dp[i-1] + dp[i]
                if v == 1:
                    dp[i] = 0
        return dp[-1]

# @lc code=end
s = Solution()
ret = s.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])
print(ret)