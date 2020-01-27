#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

from typing import List

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return len(chars)
        head = 1
        compare_idx = 0
        store_idx = 0
        n = len(chars)
        chars.append(None)
        while head <= n:
            if chars[compare_idx] == chars[head]:
                head += 1
            else:
                count = head - compare_idx
                chars[store_idx] = chars[compare_idx]
                if count > 1:
                    count = str(count)
                    for char in count:
                        store_idx += 1
                        chars[store_idx] = char
                store_idx += 1
                compare_idx = head
                head += 1
        while store_idx < len(chars):
            chars.pop(-1)
        return len(chars)

# @lc code=end
s = Solution()
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b","c","c"]
ret = s.compress(chars)
print(ret, chars)
