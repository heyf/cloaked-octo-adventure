# 4. Median of Two Sorted Arrays - LeetCode
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        left1 = 0
        left2 = 0
        right1 = len(nums1) - 1
        right2 = len(nums2) - 1
        total = len(nums2) + len(nums1)
        odd = ( total ) % 2
        while total > 2:
            # Pop Left
            if left1 <= right1 and left2 <= right2:
                if nums1[left1] < nums2[left2]:
                    left1 += 1
                else:
                    left2 += 1
            elif left1 > right1: # num1 null
                left2 += 1
            elif left2 > right2:
                left1 += 1
            # Pop Right
            if right1 >= left1 and right2 >= left2:
                if nums1[right1] > nums2[right2]:
                    right1 -= 1
                else:
                    right2 -= 1
            elif right2 < left2: # num2 null
                right1 -= 1
            elif right1 < left1:
                right2 -= 1
            total -= 2
        if odd:
            if (left2 - 1) == right2:
                return nums1[left1]
            elif (left1 - 1) == right1:
                return nums2[left2]
        else:
            if (left1 - 1) == right1: # left empty
                return (nums2[left2] + nums2[right2]) / 2.0
            elif (left2 - 1) == right2: # right empty
                return (nums1[left1] + nums1[right1]) / 2.0
            else:
                return ( nums1[left1] + nums2[left2] ) / 2.0
        
ans = [
    ([1],[1],1),
    ([1,2],[3],2),
    ([1,2,3],[4],2.5),
    ([4],[1,2,3],2.5),
]

s = Solution()
for i in ans:
    r = s.findMedianSortedArrays(i[0],i[1])
    print r, r == i[2]