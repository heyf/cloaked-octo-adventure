# Number of Closed Islands - LeetCode Contest
# https://leetcode.com/contest/weekly-contest-162/problems/number-of-closed-islands/

from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n_rols = len(grid)
        n_cols = len(grid[0])
        # remove land: DFS
        def remove_land(r,c):
            if r < 0 or c < 0 or r >= n_rols or c >= n_cols or grid[r][c] == 1:
                return
            else:
                grid[r][c] = 1
                remove_land(r-1,c)
                remove_land(r+1,c)
                remove_land(r, c-1)
                remove_land(r, c+1)
            return
        for r in range(n_rols):
            remove_land(r, 0)
            remove_land(r, n_cols-1)
        for c in range(n_cols):
            remove_land(0, c)
            remove_land(n_rols-1, c)

        # get island: DFS
        def get_island(r,c):
            if r < 0 or c < 0 or r >= n_rols or c >= n_rols or grid[r][c] == 1:
                return
            else:
                grid[r][c] = 1
                get_island(r-1, c)
                get_island(r+1, c)
                get_island(r, c-1)
                get_island(r, c+1)
            return
        
        label_count = 0
        for r in range(n_rols):
            for c in range(n_cols):
                if grid[r][c] == 0:
                    get_island(r, c)
                    label_count += 1
        return label_count

s = Solution()
# grid = [
#     [1,1,1,1,1,1,1],
#     [1,0,0,0,0,0,1],
#     [1,0,1,1,1,0,1],
#     [1,0,1,0,1,0,1],
#     [1,0,1,1,1,0,1],
#     [1,0,0,0,0,0,1],
#     [1,1,1,1,1,1,1]
# ]
# WA1:
grid = [
    [1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0],
    [1,0,1,0,1,1,1,0],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0]
] #2

# WA2: expected 6
grid = [
    [0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1],
    [0,1,1,0,0,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1],
    [1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,0,1,0,0],
    [0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0],
    [1,1,0,0,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1],
    [1,1,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0],
    [1,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,0,0,0],
    [1,1,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,1,1],
    [1,0,0,1,1,1,1,0,1,0,1,1,1,0,0,0,0,1,1,0],
    [1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,1,1],
    [0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,1,0,0,0],
    [1,0,0,0,1,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1]]
ret = s.closedIsland(grid)
print(ret)