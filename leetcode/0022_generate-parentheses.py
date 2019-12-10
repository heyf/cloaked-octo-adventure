#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import List

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def helper(out, left, right):
            if left == 0 and right == 0:
                ret.append(out)
            if left <= right:
                if left > 0:
                    helper(out+'(', left - 1, right)
                if right > 0:
                    helper(out+')', left, right - 1)

        helper("",n,n)
        return ret

# @lc code=end
s = Solution()
ret = s.generateParenthesis(3)
print(ret)