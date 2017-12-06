## 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end = len(nums)
        start = 0
        while start < end - 1:
            current = nums[ start ]
            if nums[ start + 1 ] == current:
                nums.pop(start+1)
                end -= 1
                continue
            start += 1
        return len(nums)

s = Solution()

a = [1,1,2,2,2,3,3,3,3,6,7,7,8,9,9,9,9,9,9,10]
# a = []
# a = [2]
# a = [1,2,2]
print s.removeDuplicates(a)
print a