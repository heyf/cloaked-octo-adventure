# 35. Search Insert Position - LeetCode
# https://leetcode.com/problems/search-insert-position/description/

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1
# Example 3:

# Input: [1,3,5,6], 7
# Output: 4
# Example 1:

# Input: [1,3,5,6], 0
# Output: 0

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in xrange(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
        
s = Solution()

a = [1,3,5,6]
b = 0

print s.searchInsert(a,b)
# print a