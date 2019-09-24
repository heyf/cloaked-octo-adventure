#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        buffer_start, buffer_end = intervals[0]
        ret = []
        for item in intervals[1:]:
            start, end = item
            if start > buffer_end:
                ret.append([buffer_start,buffer_end])
                buffer_start, buffer_end = start, end
            else:
                buffer_end = end
        ret.append([buffer_start, buffer_end])
        return ret

# s = Solution()
# print(s.merge([[1,3],[2,4]]))

