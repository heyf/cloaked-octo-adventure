# 136. Single Number - LeetCode
# https://leetcode.com/problems/single-number/description/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]
    
s = Solution()
print s.singleNumber(range(10000)+range(9999))
