#!/usr/bin/python3
# 119. Pascal's Triangle II - LeetCode
# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution(object):
    def __init__(self):
        self.result = {
            0: [1],
            1: [1,1],
        }
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if self.result.get(rowIndex):
            return self.result.get(rowIndex)
        last_row = self.getRow(rowIndex-1)
        if last_row:
            row_res = [1]
            j = 1
            while j < rowIndex:
                row_res.append( last_row[j-1] + last_row[j] )
                j += 1
            row_res.append(1)
            self.result[rowIndex] = row_res
            return row_res
        
s = Solution()
print(s.getRow(3))