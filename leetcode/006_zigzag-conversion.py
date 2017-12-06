'''
6. ZigZag Conversion
https://leetcode.com/problems/zigzag-conversion/

'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        row, step = -1, 1
        buff = [ str() for i in range(numRows) ]
        for i in range(len(s)):
            if row == numRows - 1:
                step = -1
            if row == 0:
                step = 1
            row += step
            buff[row] += s[i]
        return ''.join(buff)
        

# TLE version
#         if numRows <= 0 or len(s) == 0:
#             return ''
#         if numRows == 1 or len(s) < numRows:
#             return s
        
#         ret = list()
#         c = 2 * ( numRows - 1 )
#         for row in xrange(numRows): # traversal each row
#             for i in xrange(row,len(s)): 
#                 zid = i % c
#                 if zid < numRows and zid == row:
#                     ret.append(s[i])
#                 if zid >= numRows and c - zid == row:
#                     ret.append(s[i])
#         return ''.join(ret)

# when r = 3 
# ''.join([s[i] for i in range(0,l,4)]+
# [s[i] for i in range(1,l,2)]+[s[i] for i in range(2,l,4)])

def test():
    cases = list()
    cases.append( ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR") )
    cases.append( ("31415926535897", 4, "32919687455513") )
    cases.append( ("A", 1, "A") )
#     cases.append( ("Asadasd", -1, "") )
#     cases.append( ("A", 0, "") )
    cases.append( ("", 3, "") )
    
    def verify(case):
        s = Solution()
        print s.convert(case[0],case[1])
        return s.convert(case[0],case[1]) == case[2]
        
    result = filter(verify, cases)
    return len(result) == len(cases), len(result), len(cases)
        
test()