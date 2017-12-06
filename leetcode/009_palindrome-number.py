'''
9. Palindrome Number | LeetCode OJ
https://leetcode.com/problems/palindrome-number/
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        filt = 10
        while ( x / filt >= 10 ):
            filt *= 10
    
        while filt > 0:
            if (( x / filt ) - x % 10 ) % 10 == 0:
                x /= 10
                filt /= 100
            else:
                return False

        return True
    
def test():
    cases = list()
    cases.append( (-1, False) )
    cases.append( (0,True) )
    cases.append( (1221, True) )
    cases.append( (1234554321,True) )
    cases.append( (1234,False) )
    
    def verify(case):
        s = Solution()
        return s.isPalindrome(case[0]) == case[1]
        
    result = filter(verify, cases)
    return len(result) == len(cases), len(result), len(cases)
        
test()