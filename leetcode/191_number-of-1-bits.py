# 191. Number of 1 Bits - LeetCode
# https://leetcode.com/problems/number-of-1-bits/description/
    
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += n % 2
            n /= 2
        return count

ans = [
    (0,0),
    (11,3),
    (2 ** 32 - 1,32),
]
        
s = Solution()
for i in ans:
    r = s.hammingWeight(i[0])
    print r, r == i[1]