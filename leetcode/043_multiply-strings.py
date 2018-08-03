# 43. Multiply Strings - LeetCode
# https://leetcode.com/problems/multiply-strings/description/

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        for i in range(len(num1)+len(num2)):
            res.append(0) 
        if num1 == "" or num2 == "":
            return ""
        if num1 == "0" or num2 == "0":
            return "0"
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j] += int(num1[-1-i]) * int(num2[-1-j])
        carry = 0
        for i in range(len(res)):
            res[i] += carry
            carry = res[i] // 10
            res[i] = res[i] % 10
        flag = True
        ret = ""
        for i in res[::-1]:
            if flag:
                if i != 0:
                    flag = False
                else:
                    continue
            ret += str(i)
        return ret
        
s = Solution()
ans = [
    ["","",""],
    ["0","0","0"],
    ["1","0","0"],
    ["1","2","2"],
    ["11","11","121"],
    ["111","111","12321"],
    ["999","999","998001"],
    ["123","321","39483"],
    ["12","3456","41472"],
    ["123","456","56088"],
]

for i in ans:
    r = s.multiply(i[0],i[1])
    print("O" if r == i[2] else "X", r)