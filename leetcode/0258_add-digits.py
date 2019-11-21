#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 > 0:
            prev_num = num
            new_num = 0
            while prev_num > 0:
                new_num += prev_num % 10
                prev_num //= 10
            num = new_num

        return num

# @lc code=end
s = Solution()
num = 38
ret = s.addDigits(num=num)
print(ret)
