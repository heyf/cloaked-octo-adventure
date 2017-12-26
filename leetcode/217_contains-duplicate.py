# 217. Contains Duplicate - LeetCode
# https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
ans = [
    ([],False),
    ([2],False),
    ([2,2],True),
    ([1,2],False),
    ([1,2,3,2],True),
    ([500]+range(1000),True),
    (range(10000),False),
]

s = Solution()
for i in ans:
    r = s.containsDuplicate(i[0])
    print r, r == i[1]