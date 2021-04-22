# Last Moment Before All Ants Fall Out of a Plank - LeetCode Contest
# https://leetcode.com/contest/weekly-contest-196/problems/last-moment-before-all-ants-fall-out-of-a-plank/

from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not left:
            return n-min(right)
        if not right:
            return max(left)
        return max(n-min(right), max(left))

s = Solution()

# ret = s.getLastMoment(n = 4, left = [4,3], right = [0,1])
# ret = s.getLastMoment(n = 7, left = [], right = [0,1,2,3,4,5,6,7])
ret = s.getLastMoment(n=9, left = [5], right = [4])
print(ret)