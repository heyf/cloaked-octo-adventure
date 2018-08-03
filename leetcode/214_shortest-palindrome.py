'''
214. Shortest Palindrome - LeetCode
https://leetcode.com/problems/shortest-palindrome/description/
'''

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        def check(l,r):
            j = 1
            while (l - j) >= 0 and (r + j) < len(s):
                if s[ l - j ] != s [ r + j ]:
                    break
                j += 1
            if l - j >= 0:
                return None
            return s[-1:r+j-1:-1] + s
        center = ( len(s) - 1 ) // 2
        for i in range( center, -1, -1 ):
            if s[i] == s[i+1]:
                res = check( i, i+1 )
                if res:
                    return res
            res = check( i,i )
            if res:
                return res
        return ""
        
ans = [
    ["aacecaaa","aaacecaaa"],
    ["abcd","dcbabcd"],
    ["",""],
    ["a","a"],
    ["baabc","cbaabc"],
]
s = Solution()
%timeit s.shortestPalindrome( 50000*"a" )
%timeit s.shortestPalindrome( 50001*"a" )
for i in ans:
    ret = s.shortestPalindrome(i[0])
    print("O" if ret == i[1] else "X", ret)