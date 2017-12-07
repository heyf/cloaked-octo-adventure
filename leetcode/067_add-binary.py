''' 67. Add Binary - LeetCode
https://leetcode.com/problems/add-binary/description/
'''

# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = 1
        m = max(len(a),len(b))
        z = 0
        res = ""
        while i < m + 1:
            x = int(a[len(a)-i]) if i <= len(a) else 0
            y = int(b[len(b)-i]) if i <= len(b) else 0
            t = x + y + z
            print x, y, z # debug
            if t > 1:
                z = 1
            else:
                z = 0
            if t % 2:
                res = "1" + res
            else:
                res = "0" + res
            i += 1
        if z == 1:
            res = "1" + res
        return res
        
        
s = Solution()

pairs = [
    (("10","1"),"11"),
    (("111","1"),"1000"),
    (("101","11"),"1000"),
    (("1110011","10001"),"10000100")
]

for i in pairs:
    res = s.addBinary(i[0][0],i[0][1])
    print res, res == i[1]