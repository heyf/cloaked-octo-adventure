from typing import List

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        ''''''
        col_upper = []
        col_lower = []
        for c in colsum:
            flag = c // 2
            upper -= flag
            lower -= flag
            col_upper.append(flag)
            col_lower.append(flag)
        for idx, c in enumerate(colsum):
            if c == 1:
                if upper > 0:
                    col_upper[idx] = 1
                    upper -= 1
                elif lower > 0:
                    col_lower[idx] = 1
                    lower -= 1
                else:
                    return []
        return [ col_upper, col_lower ]

s = Solution()
# ret = s.reconstructMatrix(upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,1,1])
# If no valid solution exists, return an empty 2-D array.
# WA1
ret = s.reconstructMatrix(2,
3,
[2,2,1,1]) # []
print(ret)