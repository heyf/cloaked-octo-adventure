# 344. Reverse String - LeetCode
# https://leetcode.com/problems/reverse-string/description/

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start = 0
        end = len(s) - 1
        while end > start:
            t = s[end]
            s[end] = s[start]
            s[start] = t
            end -= 1
            start += 1
        return "".join(s)
        
ans = [
    ("abcde","edcba"),
    ("a","a"),
    ("",""),
]
s = Solution()
for i in ans:
    r = s.reverseString(i[0])
    print r, r == i[1]