# Cells with Odd Values in a Matrix - LeetCode Contest
# https://leetcode.com/contest/weekly-contest-162/problems/cells-with-odd-values-in-a-matrix/

from typing import List

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        '''oddCells'''
        ris = [ 0 for i in range(n)]
        cis = [ 0 for i in range(m)]
        count = 0
        for ri, ci in indices:
            ris[ri] += 1
            cis[ci] += 1
        for r in range(n):
            for c in range(m):
                if ris[r] + cis[c] % 2 == 1:
                    count += 1
        return count

s = Solution()
# print(s.oddCells(n = 2, m = 3, indices = [[0,1],[1,1]]))
# print(s.oddCells(n = 2, m = 2, indices = [[1,1],[0,0]]))
# WA1
res = s.oddCells(
    n=28,
    m=38,
    indices=[
        [17,16],[26,31],[19,12],[22,24],[17,28],[23,21],[27,32],
        [23,27],[23,33],[18,7],[4,20],[0,31],[25,33],[5,22]
]) #460
print(res) 