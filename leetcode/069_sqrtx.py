''' 69. Sqrt(x) - LeetCode
https://leetcode.com/problems/sqrtx/description/
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        res = 0
        divide = 1
        while x / divide >= 1:
            divide *= 100
        while divide >= 1:
            y = x / divide
            i = 9
            while i > -1:
                r = ( 20 * res + i) * i
                if r <= y:
                    res = res * 10 + i
                    x -= r * divide
                    divide /= 100
                    break
                i -= 1
        return res
        
s = Solution()

pairs = [
    (0,0),
    (1.5,1),
    (4,2),
    (732.57,27),
    (123456,351),
]

for i in pairs:
    res = s.mySqrt(i[0])
    print res, res == i[1]