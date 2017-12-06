'''
13. Roman to Integer | LeetCode OJ
https://leetcode.com/problems/roman-to-integer/
'''

'''
I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和M（1000）
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        ret = 0
        
        for i in xrange(len(s)-1):
            if not values.has_key(s[i]): # error happened
                return 0
            ret += values.get(s[i]) * ( -1 if values.get(s[i]) < values.get(s[i+1]) else 1 )
            
        return ret + values.get(s[-1])
        
            
def test():
    cases = list()
    cases.append( ('I', 1) )
    cases.append( ('IV', 4) )
    cases.append( ('VIII', 8) )
    cases.append( ('XX', 20) )
    cases.append( ('XXI', 21) )
    cases.append( ('XCIX', 99) )
    cases.append( ('XIV', 14) )
    
    cases.append( ('XLV', 45) )
    
    def verify(case):
        s = Solution()
        return s.romanToInt(case[0]) == case[1]
    
    def run():
        s = Solution()
        return map( s.romanToInt, [case[0] for case in cases] )
            
    result = filter(verify, cases)
    print run()
    
    return len(result) == len(cases), len(result), len(cases)

test()