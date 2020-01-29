#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

from typing import List

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points = sorted(points, key=lambda x: x[0])
        res = 1
        shot = points[0][1]
        for p in points[1:]:
            if p[0] <= shot:
                shot = min(shot, p[1])
            else:
                res += 1
                shot = p[1]
        return res

# @lc code=end
# points = [[10,16], [2,8], [1,6], [7,12]]
points = [[1,2],[2,3],[3,4],[4,5]] # WA1, 2
s = Solution()
ret = s.findMinArrowShots(points)
print(ret)
