#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] =="0":
            return 0
        dp = [ 0 for i in range(len(s)+1)]
        dp[-1] = 1
        dp[0] = 1
        for i, v in enumerate(s[1:], start=1):
            if v == "0":
                dp[i] = 0 if s[i-1] > "2" or s[i-1] == "0" else dp[i-2]
            elif v > "6":
                if s[i-1] == "1":
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                if s[i-1] == "1" or s[i-1] == "2":
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[len(s)-1]

# @lc code=end
s = Solution()
ret = s.numDecodings("100")
print(ret)