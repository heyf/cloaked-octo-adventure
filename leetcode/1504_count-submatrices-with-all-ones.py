# Count Submatrices With All Ones - LeetCode Contest
# https://leetcode.com/contest/weekly-contest-196/problems/count-submatrices-with-all-ones/

from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        result_dict = {}
        def helper(m, n):
            if result_dict.get((m, n)) is None:
                pass


            return result_dict.get((m, n))
        return 0