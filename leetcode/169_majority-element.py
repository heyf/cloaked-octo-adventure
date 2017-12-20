# 169. Majority Element - LeetCode
# https://leetcode.com/problems/majority-element/description/

# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]
        
s = Solution()
print s.majorityElement([1,2,3,1,1,1,1])
print s.majorityElement([1,2,3,2,2,2,1])