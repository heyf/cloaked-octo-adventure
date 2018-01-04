# 12. Integer to Roman - LeetCode
# https://leetcode.com/problems/integer-to-roman/description/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = [
            ("M",1000),
            ("CM",900),
            ("D",500),
            ("CD",400),
            ("C",100),
            ("XC",90),
            ("L",50),
            ("XL",40),
            ("X",10),
            ("IX",9),
            ("V",5),
            ("IV",4),
            ("I",1),
        ]
        ret = ""
        for c, n in d:
            while num >= n:
                ret += c
                num -= n
        return ret
    
ans = [
    ("MMMCCCXXXIII",3333),
    ("MMM",3000),
    ("MCDXXXVII",1437),
    ("MD", 1500),
    ("XL",40)
]

s = Solution()
for i in ans:
    r = s.intToRoman(i[1])
    print r, r == i[0]