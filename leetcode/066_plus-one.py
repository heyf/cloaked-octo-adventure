''' 66. Plus One - LeetCode
https://leetcode.com/problems/plus-one/description/
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plus = 1
        for i in xrange(len(digits)-1,-1,-1):
            if plus == 0:
                break
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                plus = 0
        if plus == 1:
            digits.insert(0,1)
        return digits
        
        
s = Solution()

pairs = [
    ([1,9],[2,0]),
    ([9],[1,0]),
    ([1,2,2],[1,2,3])
]

for i in pairs:
    res = s.plusOne(i[0])
    print res, i[1] == res