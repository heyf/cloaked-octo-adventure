#!/usr/bin/python3
# 118. Pascal's Triangle - LeetCode
# https://leetcode.com/problems/pascals-triangle/description/

class Solution(object):  
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1,numRows):
            row_res = [1]
            j = 1
            while j < i:
                row_res.append( res[i-1][j-1] + res[i-1][j] )
                j += 1
            row_res.append(1)
            res.append(row_res)
        return res
            

s = Solution()
print(s.generate(0))
print(s.generate(5))