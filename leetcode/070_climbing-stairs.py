'''70. Climbing Stairs - LeetCode
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.'''

class Solution(object):
    def __init__(self):
        self.results = {
            1: 1,
            2: 2,
            3: 3,
        }

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if self.results.has_key(n):
            return self.results.get(n)
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.results[n] = res
        return res
    
pairs = [
    (1,1),
    (2,2),
    (3,3),
    (4,5),
    (5,8),
    (35,14930352),
]

s = Solution()

for i in pairs:
    res = s.climbStairs(i[0])
    print res, res == i[1]