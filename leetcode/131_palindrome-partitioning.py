#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

from typing import List

'''
DFS

Runtime: 808 ms, faster than 10.45% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 30.5 MB, less than 33.73% of Python3 online submissions for Palindrome Partitioning.
'''

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        out = []
        res = []

        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def helper(start):
            if start >= n:
                res.append(out.copy())
                return
            
            for i in range(start, n):
                if not is_palindrome(start, i):
                    continue
                out.append(s[start:i+1])
                helper(i+1)
                out.pop(-1)

        helper(0)
        return res

# @lc code=end
s = Solution()
s_in = "aab"

print(s.partition(s_in))
