#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

from typing import List

'''
DFS+Cache

Runtime: 668 ms, faster than 50.33% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 30.5 MB, less than 23.18% of Python3 online submissions for Palindrome Partitioning.
'''

# @lc code=start

from functools import lru_cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        out = []
        res = []

        @lru_cache(maxsize=None)
        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def helper(start):
            if start >= n:
                # 注意：添加要调用 .copy 添加一个副本，否则会添加索引
                res.append(out.copy())
                return
            
            for i in range(start, n):
                if not is_palindrome(start, i):
                    continue
                out.append(s[start:i+1]) # 注意开闭区间，is_palindrome 是左闭右闭判断的，循环条件是左闭右开
                helper(i+1)
                out.pop(-1)

        helper(0)
        return res

# @lc code=end
s = Solution()
s_in = "aab"

print(s.partition(s_in))
