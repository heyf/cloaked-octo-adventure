#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
from typing import List

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(start, end):
            if start >= end:
                return start
            pivot = end
            store_index = start
            for i in range(start, end):
                if nums[i] > nums[pivot]:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1
            nums[pivot], nums[store_index] = nums[store_index], nums[pivot]
            return store_index
        pivot = len(nums) - 1
        start, end = 0, pivot
        pivot = partition(start, end)
        while pivot != k-1:
            if pivot < k-1:
                start, end = pivot+1, end
            elif pivot > k-1:
                start, end = start, pivot-1
            else:
                break
            pivot = partition(start, end)
        return nums[pivot]

# @lc code=end
s = Solution()
# nums = [1,4,2,8,5,7,3,9]
# k = 6
# WA1
# nums = [3,2,1,5,6,4]
# k = 2
# WA2
# nums = [2,1]
# k = 1
# WA3
nums = [-1,2,0]
k = 3
ret = s.findKthLargest(nums, k)
print(ret)