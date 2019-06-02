# 1046. Last Stone Weight - LeetCode Contest
# https://leetcode.com/contest/weekly-contest-137/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones = sorted(stones,reverse=True)
        while len(stones) > 1:
            first_stone = stones.pop(0)
            second_stone = stones.pop(0)
            if first_stone > second_stone:
                remains = first_stone - second_stone
                i = 0
                while i < len(stones) and stones[i] > remains:
                    i += 1
                stones.insert(i,remains)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0

s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))