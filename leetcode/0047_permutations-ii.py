#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

from typing import List

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        if nums:
            ret = [[]]
            for i in nums:
                new_ret = []
                for lst in ret:
                    idx = 0
                    while idx < len(lst)+1:
                        new_lst = lst.copy()
                        while idx < len(lst) and lst[idx] == i:
                            idx += 1
                        new_lst.insert(idx, i)
                        new_ret.append(new_lst)
                        idx += 1
                ret = new_ret
        return ret

# @lc code=end
# nums = [1,1,2,1]
nums = [2,2,1,1] # WA1
s = Solution()
ret = s.permuteUnique(nums)
print(ret)