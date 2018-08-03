# 128. Longest Consecutive Sequence - LeetCode
# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lrdict = dict()
        ret = 0
        for i in nums:
            if lrdict.get(i) is not None:
                continue
            if lrdict.get(i-1) is not None and lrdict.get(i+1) is not None:
                lrdict[i] = i
            l = lrdict.get(i-1,i)
            r = lrdict.get(i+1,i)
            lrdict[l] = r
            lrdict[r] = l
            ret = max( ret, r - l + 1 )
        return ret
        
ans = [
    ([100, 4, 200, 1, 3, 2],4),
    ([0,-1],2),#WA1
    ([-2,-3,-3,7,-3,0,5,0,-8,-4,-1,2],5),#WA2
    ([-6,6,-9,-7,0,3,4,-2,2,-1,9,-9,5,-3,6,1,5,-1,-2,9,-9,-4,-6,-5,6,-1,3],14)#WA3
]

s = Solution()

for i in ans:
    r = s.longestConsecutive(i[0])
    print( "O" if r == i[1] else "X", r)