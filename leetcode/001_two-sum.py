'''
1. Two Sum
https://leetcode.com/problems/two-sum/
Runtime: 5856 ms
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

def test():
    cases = list()

    cases.append(([1,2,3,4],7,[2,3]))
    cases.append(([2,7,11,15],9,[0,1]))
    cases.append(([1,2,3,4,5,6,7,8,9,10],7,[0,5]))
    cases.append((list(range(1,1000)),58,[0,56]))

    def verify(case):
        nums = case[0]
        target = case[1]
        answer = case[2]
        s = Solution()
        return s.twoSum(nums, target) == answer
        
    result = filter(verify, cases)
    return len(result) == len(cases), len(result), len(cases)
    
test()