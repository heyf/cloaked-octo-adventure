# 202. Happy Number - LeetCode
# https://leetcode.com/problems/happy-number/description/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def calc(x):
            ret = 0
            while x > 0:
                ret += ( x % 10 ) ** 2
                x /= 10
            return ret
        traveled = {}
        r = n
        while True:
            if traveled.has_key(r):
                return False
            traveled.update({r:True})
            r = calc(r)
            if r == 1:
                return True
                        
s = Solution()
ans = [
    (0,False),
    (1,True),
    (2,False),
    (4,False),
    (16,False),
    (37,False),
    (58,False),
    (89,False),
    (145,False),
    (42,False),
    (20,False),
    (19,True),
    (82,True),
    (68,True),
    (100,True),
]
for i in ans:
    r = s.isHappy(i[0])
    print r, r == i[1]