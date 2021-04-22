# 1394. Find Lucky Integer in an Array - LeetCode
# https://leetcode.com/problems/find-lucky-integer-in-an-array/

from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        if not arr:
            return -1
        arr = sorted(arr)
        i = len(arr) - 1
        num = arr[i]
        count = 1
        i -= 1
        while i > -1:
            if arr[i] != num:
                if count == num:
                    return num
                else:
                    num = arr[i]
                    count = 1
            else:
                count += 1
            i -= 1
        
        if count == num:
            return num

        return -1

arr = [7,7,7,7,7,7,7]

s = Solution()
ret = s.findLucky(arr)
print(ret)
