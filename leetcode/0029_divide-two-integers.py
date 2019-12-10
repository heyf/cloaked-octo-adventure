#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
INT_MAX = 2 ** 31 - 1

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        m, n = abs(dividend), abs(divisor)
        ret = 0
        if n == 1:
            ret = m
        else:
            while m >= n:
                t, p = n, 1
                while m >= (t << 1):
                    t <<= 1
                    p <<= 1
                ret += p
                m -= t
        
        ret = -ret if (dividend > 0) ^ (divisor > 0) else ret
        if ret > INT_MAX:
            ret = INT_MAX
        return ret

# @lc code=end
s = Solution()
# ret = s.divide(7, -3)
# ret = s.divide(1, 1) # WA1
# ret = s.divide(-1,-1) # WA2
ret = s.divide(-2**31-1, 1)
print(ret)