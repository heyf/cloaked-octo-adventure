#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:
            return True
        if x + y < z:
            return False
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
        return (z % gcd(x, y)) == 0

# @lc code=end
s = Solution()
x, y, z = 1, 2, 4
ret = s.canMeasureWater(x, y, z)
print(ret)