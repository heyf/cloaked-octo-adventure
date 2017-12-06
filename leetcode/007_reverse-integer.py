'''
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        while x > 0:
            digit = x % 10
            x /= 10
            ret = ret * 10 + digit
        return ret * sign
        
def test():
    cases = list()
    cases.append( (0,0) )
    cases.append( (123,321) )
    cases.append( (-123,-321) )
    
    def verify(case):
        s = Solution()
        print s.reverse(case[0])
        return s.reverse(case[0]) == case[1]
        
    result = filter(verify, cases)
    return len(result) == len(cases), len(result), len(cases)
        
test()