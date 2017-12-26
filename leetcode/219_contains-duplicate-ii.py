# 219. Contains Duplicate II - LeetCode
# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_dict = dict()
        for i in range(len(nums)):
            if index_dict.has_key(nums[i]) and i - index_dict.get(nums[i]) <= k:
                return True
            else:
                index_dict.update({nums[i]:i})
        return False
        
ans = [
    ([],1,False),
    ([1],1,False),
    ([1,2,3,2],1,False),
    ([1,2,3,2],2,True),
    (range(1000) + [500],300, False),
    (range(1000) + [500],600, True),
]
s = Solution()
for i in ans:
    r = s.containsNearbyDuplicate(i[0],i[1])
    print r, r == i[2]