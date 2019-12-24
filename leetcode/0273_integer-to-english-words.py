#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        v0 = ["Thousand", "Million", "Billion"]
        v1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        v2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        ret = []

        def convert_hundred(sub_num):
            h_ret = []
            hundred = sub_num // 100
            if hundred > 0:
                h_ret.append(v1[hundred])
                h_ret.append("Hundred")
            sub_num = sub_num % 100
            if sub_num > 19:
                ten = sub_num // 10
                sub_num = sub_num % 10
                h_ret.append(v2[ten])
                if sub_num > 0:
                    h_ret.append(v1[sub_num])
            elif sub_num > 0:
                h_ret.append(v1[sub_num])
            return " ".join(h_ret)

        sub_num = num % 1000
        ret = [convert_hundred(sub_num)] + ret
        num = num // 1000
        for i in range(3):
            if num == 0:
                break
            sub_num = num % 1000
            if sub_num > 0:
                ret = [convert_hundred(sub_num), v0[i]] + ret
            num = num // 1000
        
        ret = " ".join([i for i in ret if i != ""])

        return ret if ret else "Zero"

# @lc code=end
s = Solution()
# WA1
# num = 0
# WA2
# num = 20
# WA3
num = 1000010001
ret = s.numberToWords(num)
print(f"'{ret}'")