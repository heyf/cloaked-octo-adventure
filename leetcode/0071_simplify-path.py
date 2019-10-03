#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        items = path.split("/")
        ret = []
        for i in items:
            if i in { ".", None, ""}:
                continue
            elif i == "..":
                if ret:
                    ret.pop(-1)
                continue
            else:
                ret.append(i)
        return "/" + "/".join(ret)

# @lc code=end
s = Solution()
print(s.simplifyPath("/../"))
