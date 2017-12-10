#!/usr/bin/python3
# 119. Pascal's Triangle II - LeetCode
# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution(object):
    def __init__(self):
        self.result = {
            0: [1],
            1: [1,1],
        }
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if self.result.get(rowIndex):
            return self.result.get(rowIndex)
        last_row = self.getRow(rowIndex-1)
        if last_row:
            row_res = [1]
            j = 1
            while j < rowIndex:
                row_res.append( last_row[j-1] + last_row[j] )
                j += 1
            row_res.append(1)
            self.result[rowIndex] = row_res
            return row_res
        
s = Solution()
print(s.getRow(3))


'''Solution 2: O(k)'''
#!/usr/bin/python3
# 119. Pascal's Triangle II - LeetCode
# https://leetcode.com/problems/pascals-triangle-ii/description/

#!/usr/bin/python3
# 119. Pascal's Triangle II - LeetCode
# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        for i in range(rowIndex+1):
            res.append(1)
            j = len(res) - 2
            while j > 0:
                res[j] = res[j] + res[j-1]
                j -= 1
        return res

pairs = [
    (0,[1]),
    (1,[1,1]),
    (2,[1,2,1]),
    (3,[1, 3, 3, 1]),
    (4,[1, 4, 6, 4, 1]),
    (5,[1, 5, 10, 10, 5, 1]),
    (6,[1, 6, 15, 20, 15, 6, 1]),
    (7,[1, 7, 21, 35, 35, 21, 7, 1])
]
        
s = Solution()
for i in pairs:
    print(s.getRow(i[0]), s.getRow(i[0])==i[1])