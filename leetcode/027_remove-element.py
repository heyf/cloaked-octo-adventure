# 27. Remove Element - LeetCode
# https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                continue
            i += 1
        return len(nums)
        
s = Solution()

# a = [ 3, 2, 2, 3 ]
# a = []
# a = [ 1 ]
# a = [3]
# a = [3,3]
a = [ 3, 2 ,2, 3 ]
print s.removeElement(a,3)
print a