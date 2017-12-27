# 231. Power of Two - LeetCode
# https://leetcode.com/problems/power-of-two/description/

class Solution(object):        
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        while n > 1:
            if n == 2:
                return True
            if n % 2:
                return False
            n /= 2
        return False
    
ans = [
    (0,False),
    (1,True),
    (2,True),
    (3,False),
    (4,True),
    (128,True),
    (127, False),
    (2**32,True),
    (2**32-1,False),
]

s = Solution()
for i in ans:
    r = s.isPowerOfTwo(i[0])
    print r, "O" if r == i[1] else "X"