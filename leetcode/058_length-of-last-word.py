# 58. Length of Last Word - LeetCode
# https://leetcode.com/problems/length-of-last-word/

# Input: "Hello World"
# Output: 5

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
# return the length of last word in the string.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s)
        ret = 0
        while i > 0:
            i -= 1
            if s[i] == " ":
                if ret == 0:
                    continue
                else:
                    break
            else:
                ret += 1
        return ret
    
s = Solution()

pairs = [
    ("Hello World", 5),
#     ("Suck",4),
#     ("You Suck",4),
#     ("Illution s", 1),
    ("a",1),
    ("",0),
    ("a ",1),
    ("a  ",1),
]

for i in pairs:
    res = s.lengthOfLastWord(i[0])
    print res, i[1] == res