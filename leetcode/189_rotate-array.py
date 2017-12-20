# 189. Rotate Array - LeetCode
# https://leetcode.com/problems/rotate-array/description/

# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for j in range(k):
            i = nums.pop()
            nums.insert(0,i)
            
#         # WA,
#         i = 0
#         j = nums[0]
#         k = k % len(nums) # TLE, [1],1
#         while True:
#             next_i = ( i - k ) % len(nums)
#             nums[i] = nums[next_i]
#             i = next_i
#             if i == k:
#                 nums[k] = j
#                 break
        
        
test = [
    ([1],1,[1]),
    ([1,2,3,4],7,[2,3,4,1]),
    ([1,2,3,4,5,6],2,[5,6,1,2,3,4]),
    ([1,2,3,4,5,6,7],3,[5,6,7,1,2,3,4]),
    ([1,2,3,4,5,6,7,8],3,[6,7,8,1,2,3,4,5]),
    ([1,2,3,4,5,6,7,8],4,[5,6,7,8,1,2,3,4]),
    (range(9),3,[6,7,8,0,1,2,3,4,5]),
]    
    
s = Solution()
for i in test:
    a = i[0]
    r = s.rotate(a,i[1])
    print a, a == i[2]