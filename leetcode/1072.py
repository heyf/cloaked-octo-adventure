class Solution:
    def maxEqualRowsAfterFlips(self, matrix) -> int:
        # 位运算+哈希表
        row_map = dict() # 0b01
        current_max = 0

        for i in range(len(matrix)):
            row = matrix[i]
            row_sum = 0
            flag = row[0]
            if flag == 0:
                for j in range(len(row)):
                    row_sum = (row_sum << 1) + row[j]
            else:
                for j in range(len(row)):
                    row_sum = (row_sum << 1) + (1 - row[j])
            # check exist
            if row_map.get(row_sum):
                row_map[row_sum] += 1
                current_max = max(current_max, row_map[row_sum])
            else:
                row_map[row_sum] = 1
                current_max = max(current_max, row_map[row_sum])
        return current_max

# method 1: brute force: 2^n * n^2
# method 2: co-relate n^2 * m # TLE
# method 3: 位运算+哈希表

# Note:
# 1 <= matrix.length <= 300
# 1 <= matrix[i].length <= 300

s = Solution()
# print(s.maxEqualRowsAfterFlips([[0,1],[1,0]]))
print(s.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))
