'''
8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/
'''

class Solution(object):
    def myAtoi(self, mstr):
        """
        :type str: str
        :rtype: int
        """
        res = 0
        i = 0
        
        int_max = 2 ** 31 - 1
        
        if len(mstr) == 0:
            return 0
        
        while mstr[i] == ' ': # escape %20
            i += 1
        
        sign = {
            '+': 1,
            '-':-1,
        }.get(mstr[i], None)
        
        if sign is not None:
            if len(mstr) == 1:
                return 0
            i += 1
        else:
            sign = 1
        
        while (mstr[i] >= '0' and mstr[i] <= '9'):
            res *= 10
            digit = int(mstr[i])
            if res > int_max - digit:
                return int_max if sign == 1 else -1 - int_max
            else:
                res += digit
            i += 1
            if i == len(mstr):
                break
        return res * sign

def test():
    cases = list()
    cases.append( ('0',0) )
    cases.append( ('-1',-1) )
    cases.append( ('-123',-123) )
    cases.append( ('1233',1233) )
    
    # cases.append( ( '48hh', 488 ) ) # python int() can't handle this
    cases.append( ('', 0) )
    cases.append( ('+', 0) )
    cases.append( ( '    12', 12 ) )
    cases.append( ( ' 1 2 3', 1 ) )
    cases.append( ("-2147483648", -2147483648) )
    # cases.append( ( 'a-4dcc8', -48 ) ) # is such case acceptable? # No such situation
    
    def verify(case):
        s = Solution()
        # print s.myAtoi(case[0])
        return s.myAtoi(case[0]) == case[1]
        
    result = filter(verify, cases)
    return len(result) == len(cases), len(result), len(cases)
        
test()
