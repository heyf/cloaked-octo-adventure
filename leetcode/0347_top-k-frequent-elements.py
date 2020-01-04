#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

from typing import List

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for i in nums:
            if counter.get(i):
                counter[i] += 1
            else:
                counter[i] = 1
        ret = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return [ x[0] for x in ret[:k] ]

# @lc code=end
# Example 1:
nums = [1,1,1,2,2,3]
k = 2
# Output: [1,2]

# Example 2:
# nums = [1]
# k = 1
# Output: [1]

s = Solution()
ret = s.topKFrequent(nums, k)
print(ret)
