#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        start, res = 0, 0
        for i, v in enumerate(s):
            if v == "(":
                stack.append(i)
            else:
                if not stack:
                    start = i + 1
                else:
                    stack.pop(-1)
                    if stack:
                        res = max( res, i - stack[-1] )
                    else:
                        res = max( res, i - start + 1 )
        return res


# @lc code=end
s = Solution()
print(s.longestValidParentheses("))))((()(("))
