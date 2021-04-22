# 1395. Count Number of Teams - LeetCode
# https://leetcode.com/problems/count-number-of-teams/

from typing import List

# 暴力搜索都 AC 了
# 其实有两次筛选的算法

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) <= 2:
            return 0
        count = 0
        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                for k in range(j+1,len(rating)):
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        count += 1
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        count += 1
        return count

# rating = [2,5,3,4,1]
rating = [1,2,3,4]
s = Solution()
ret = s.numTeams(rating)
print(ret)
