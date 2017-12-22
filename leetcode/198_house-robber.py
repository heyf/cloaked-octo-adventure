# 198. House Robber - LeetCode
# https://leetcode.com/problems/house-robber/description/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        i = 2
        prev_prev = nums[0]
        prev = max(nums[0],nums[1])
        while i < len(nums):
            current_max = max( nums[i] + prev_prev, prev )
            i += 1
            prev_prev = prev
            prev = current_max
        return current_max
        

# TLE
# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         if len(nums) == 2:
#             return max(nums[0],nums[1])
#         return max( nums[-1] + self.rob(nums[:-2]), nums[-2] + self.rob(nums[:-3]) )
        
ans = [
    ([],0),
    ([1],1),
    ([2,3],3),
    ([1,2,3],4),
    ([1,2,3,4],6),
    ([1,5,10,10,5,1],16),
    ([2,3,1],3),
    ([2,3,1,0,2],5),
    ([2,3,1,3,5],8),
]

s = Solution()

for i in ans:
    r = s.rob(i[0])
    print r, r == i[1]