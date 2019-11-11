#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

from typing import List

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        if nums:
            ret = [[]]
            for i in nums:
                new_ret = []
                for lst in ret:
                    for j in range(len(lst)+1):
                        new_lst = lst.copy()
                        new_lst.insert(j, i)
                        new_ret.append(new_lst)
                ret = new_ret
        return ret

# @lc code=end
nums = [1]
s = Solution()
ret = s.permute(nums)
print(ret)