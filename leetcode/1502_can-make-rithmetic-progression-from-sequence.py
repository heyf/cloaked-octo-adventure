# Can Make Arithmetic Progression From Sequence - LeetCode Contest
# https://leetcode.com/contest/weekly-contest-196/problems/can-make-rithmetic-progression-from-sequence/

from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # len(arr) >= 2
        # if not arr:
        #     return False
        # if len(arr) == 1:
        #     return True
        
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        prev = arr[1]
        for _, item in enumerate(arr[2:], start=2):
            if item - prev != diff:
                return False
            else:
                prev = item
        return True

s = Solution()

arr = [3,5,1]
ret = s.canMakeArithmeticProgression(arr)
print(ret)
