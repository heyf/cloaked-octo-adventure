# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        M = 1000000007
        ret = 0
        for i in range(k, m+1):
            ret += ((i-1)**(k-1)) * (i**(n-k))
        return ret % M


# n = 2
# m = 3
# k = 1
# ans = 6

# n = 9
# m = 1
# k = 1
# ans = 1

n = 50
m = 100
k = 25
ans = 34549172

# n = 37
# m = 17
# k = 7
# ans = 418930126

sl = Solution()
ret = sl.numOfArrays(n, m, k)
print(ret, "O" if ret==ans else "X")