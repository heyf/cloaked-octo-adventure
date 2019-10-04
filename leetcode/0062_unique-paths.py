#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ 1 for i in range(n)]
        for _ in range(1,m):
            for j in range(1,n):
                dp[j] += dp[j-1]
        return dp[-1]

# @lc code=end
s = Solution()
print(s.uniquePaths(7,3))
