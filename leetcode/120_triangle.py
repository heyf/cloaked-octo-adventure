#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

from typing import List

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if not n:
            return 0
        
        min_total = triangle[-1].copy()

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                min_total[j] = triangle[i][j] + min(min_total[j], min_total[j+1])
        
        return min_total[0]

# @lc code=end
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
s = Solution()
print(s.minimumTotal(triangle))