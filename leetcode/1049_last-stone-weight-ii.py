# 1049. Last Stone Weight II - LeetCode Contest
# https://leetcode.com/contest/weekly-contest-137/problems/last-stone-weight-ii/

class Solution:
    def lastStoneWeightII(self, stones) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        current_min = 0
        stones = sorted(stones)
        for idx_l in range(len(stones)):
            for idx_h in range(len(stones)):
                current_min = min(current_min,self.lastStoneWeightII(stones+[stones[idx_h]-stones[idx_l]]))
        return current_min


ans = [
    [[2,7,4,1,8,1],1],
    [[2,11,13,15,17],2],
    [[31,26,33,21,40],5],
]

s = Solution()
print(s.lastStoneWeightII(ans[2][0]))