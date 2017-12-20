# 171. Excel Sheet Column Number - LeetCode
# https://leetcode.com/problems/excel-sheet-column-number/description/

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        j = 1
        res = 0
        while i > -1:
            res += j * (ord(s[i]) - ord("A") + 1)
            i -= 1
            j *= 26
        return res
        
pairs = [
    ("A",1),
    ("B",2),
    ("C", 3),
    ("Z", 26),
    ("AA", 27),
    ("AB", 28),
]

s = Solution()

for i in pairs:
    r = s.titleToNumber(i[0])
    print r, r == i[1]