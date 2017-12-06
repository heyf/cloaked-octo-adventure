# 53. Maximum Subarray - LeetCode
# https://leetcode.com/problems/maximum-subarray/description/

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending_here = max_so_far = nums[0]
        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    
s = Solution()
pairs = [
    ([-2,1,-3,4,-1,2,1,-5,4],6),
    ([-1,-2],-1),
    ([1],1),
    ([2,3,4,5],14),
    ([1,-50,3],3),
    ([5,-2,4],7)
]
        
for i in pairs:
    print s.maxSubArray(i[0]), i[1] == s.maxSubArray(i[0])