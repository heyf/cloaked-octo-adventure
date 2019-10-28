#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

from typing import List

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # null check
        if not matrix and not matrix[0]:
            return
        nrows, ncols = len(matrix), len(matrix[0])
        row_zero, col_zero = False, False
        for c in range(ncols):
            if matrix[0][c] == 0:
                row_zero = True
        for r in range(nrows):
            if matrix[r][0] == 0:
                col_zero = True
        for r in range(1,nrows):
            for c in range(1,ncols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if row_zero:
            for c in range(ncols):
                matrix[0][c] = 0
        if col_zero:
            for r in range(nrows):
                matrix[r][0] = 0
        return
        
# @lc code=end
s = Solution()
wa1 = [[1,2,3,4],[5,0,5,2],[8,9,2,0],[5,7,2,1]]
a = wa1
s.setZeroes(a)
print(a)