'''
054. Spiral Matrix - LeetCode
https://leetcode.com/problems/spiral-matrix/description/
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        m = len(matrix)
        if m == 0:
            return ret
        n = len(matrix[0])
        if n == 0:
            return ret
        col = -1
        row = 0
        while True:
            for i in range(n):
                col += 1
                ret.append( matrix[row][col] )
            m -= 1
            if m == 0:
                break
            for i in range(m):
                row += 1
                ret.append( matrix[row][col] )
            n -= 1
            if n == 0:
                break
            for i in range(n):
                col -= 1
                ret.append( matrix[row][col] )
            m -= 1
            if m == 0:
                break
            for i in range(m):
                row -= 1
                ret.append( matrix[row][col] )
            n -= 1
            if n == 0:
                break
        return ret
        
ans = [
    [
        [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ], 
        [1,2,3,6,9,8,7,4,5]
    ],
    [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9,10,11,12]
        ],
        [1,2,3,4,8,12,11,10,9,5,6,7]
    ],
    [
        [],
        []
    ],
    [
        [[]],
        []
    ],
]

s = Solution()
for i in ans:
    ret = s.spiralOrder(i[0])
    print( "O" if ret == i[1] else "X", ret )