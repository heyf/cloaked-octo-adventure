# 167. Two Sum II - Input array is sorted - LeetCode
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 1
        right = len(numbers)
        while True:
            sums = numbers[left-1] + numbers[right-1]
            if sums == target:
                return [ left, right ]
            elif sums > target:
                right -= 1
            else:
                left += 1
        
test_case = [
    ( [1,2,3,4,5,6,7,8], 5, [1,4] ),
    ( [2,7,11,15], 9, [1,2] ),
]
s = Solution()
for i in test_case:
    r = s.twoSum(i[0],i[1])
    print r, r == i[2]