# 172. Factorial Trailing Zeroes - LeetCode
# https://leetcode.com/problems/factorial-trailing-zeroes/description/

# Given an integer n, return the number of trailing zeroes in n!.
# Note: Your solution should be in logarithmic time complexity.

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        j = 5
        while n / j > 0:
            res += n/j
            j *= 5
        return res
    
s = Solution()
print s.trailingZeroes(25)