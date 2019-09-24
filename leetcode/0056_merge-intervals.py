#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        buffer_start, buffer_end = intervals[0]
        ret = []
        for item in intervals[1:]:
            start, end = item
            if start > buffer_end:
                ret.append([buffer_start,buffer_end])
                buffer_start, buffer_end = start, end
            else:
                buffer_end = max(buffer_end, end)
        ret.append([buffer_start, buffer_end])
        return ret

# class Test:
#     @staticmethod
#     def test():
#         ans = [
#             {"input":{"intervals":[[1,3],[2,4]]},"output":[[1,4]]},
#             {"input":{"intervals":[]},"output":[[]]},
#         ]
#         s = Solution()
#         for i in ans:
#             assert str(s.merge(**i["input"])) == str(i["output"])

# Test.test()
