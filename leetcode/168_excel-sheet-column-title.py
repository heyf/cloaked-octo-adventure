# 168. Excel Sheet Column Title - LeetCode
# https://leetcode.com/problems/excel-sheet-column-title/description/

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = ""
        while n > 0:
            if n % 26 == 0:
                ret = "Z" + ret
                n -= 26
            else:
                ret = chr( ( 64 + n % 26)  ) + ret
            n /= 26
        return ret
        

s = Solution()
print s.convertToTitle( 1 )
print s.convertToTitle( 26 )
print s.convertToTitle( 27 )
print s.convertToTitle( 2000 )
print s.convertToTitle( 26*26 + 26 ) # ZZ
print s.convertToTitle( 26*26 + 26 + 1) # AAA