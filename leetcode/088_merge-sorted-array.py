'''88. Merge Sorted Array - LeetCode
https://leetcode.com/problems/merge-sorted-array/description/'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        while i >= 0:
            if j < 0:
                return
            if nums1[i] > nums2[j]:
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1
        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1
        return

s = Solution()

pairs = [
    [[[1,3,4,5,6,8,10,0,0,0],7,[2,7,9],3],[1,2,3,4,5,6,7,8,9,10]],
    [[[1,3,4,5,6,8,10],7,[],0],[1,3,4,5,6,8,10]],
    [[[0,0],0,[1,2],2],[1,2]],
]

for i in pairs:
    s.merge(i[0][0],i[0][1],i[0][2],i[0][3])
    print i[0][0], i[0][0] == i[1]