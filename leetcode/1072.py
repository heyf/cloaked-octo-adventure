class Solution:
    def maxEqualRowsAfterFlips(self, matrix) -> int:
        row_flags = [ False for i in range(len(matrix)) ]
        current_max = 1

        def correlate_check(source_row,target_row):
            source = matrix[source_row]
            target = matrix[target_row]
            delta = source[0] == target[0]
            for i in range(1,len(source)):
                if (source[i] == target[i]) != delta:
                    return False
            else:
                return True

        for row_index in range(len(matrix)):
            if row_flags[row_index]:
                continue
            same_row = 1
            for i in range(row_index+1,len(matrix)):
                if row_flags[row_index]:
                    continue
                if correlate_check(row_index,i):
                    row_flags[i] = True
                    same_row += 1
                    current_max = max(same_row,current_max)
        return current_max

# method 1: brute force: 2^n * n^2
# method 2: co-relate
s = Solution()
print(s.maxEqualRowsAfterFlips([[0,1],[1,0]]))
# print(s.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))

# 001
# 110