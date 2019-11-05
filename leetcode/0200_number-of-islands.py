#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

from typing import List

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        def DFS(i,j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if grid[i][j] == "1":
                grid[i][j] = "0"
                DFS(i+1, j)
                DFS(i-1, j)
                DFS(i, j+1)
                DFS(i, j-1)
                return 1
            return 0
                
        count = 0
        for i in range(m):
            for j in range(n):
                count += DFS(i, j)

        return count

# @lc code=end
# a = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
# ]
a = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
s = Solution()
print(s.numIslands(a))