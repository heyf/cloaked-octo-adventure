'''
059. Spiral Matrix II - LeetCode
https://leetcode.com/problems/spiral-matrix-ii/description/
'''

# import numpy as np

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
#         ret = np.zeros((n,n),dtype=int)
        ret = []
        for i in range(n):
            ret.append([])
            for j in range(n):
                ret[i].append(0)
        col = -1
        row = 0
        x = n
        y = n
        j = 1
        while True:
            for i in range(x):
                col += 1
                ret[row][col] = j
                j += 1
            y -= 1
            if y == 0:
                break
            for i in range(y):
                row += 1
                ret[row][col] = j
                j += 1
            x -= 1
            if x == 0:
                break
            for i in range(x):
                col -= 1
                ret[row][col] = j
                j += 1
            y -= 1
            if y == 0:
                break
            for i in range(y):
                row -= 1
                ret[row][col] = j
                j += 1
            x -= 1
            if x == 0:
                break
        return ret

ans = [
    [
        3,
        [
         [ 1, 2, 3 ],
         [ 8, 9, 4 ],
         [ 7, 6, 5 ]
        ]
    ]
]
    
s = Solution()
for i in ans:
    ret = s.generateMatrix(i[0])
#     print( "O" if (ret == i[1]).all() else "X", ret)
    print( "O" if ret == i[1] else "X", ret)