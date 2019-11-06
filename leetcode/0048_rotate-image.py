#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

from typing import List

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n-1):
            for j in range(n-i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        return

# @lc code=end
a = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s = Solution()
s.rotate(a)
print(a)
