# 190. Reverse Bits - LeetCode
# https://leetcode.com/problems/reverse-bits/description/

# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
# return 964176192 (represented in binary as 00111001011110000010100101000000).

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        count = 0
        ret = 0
        while n > 0 or count < 32:
            ret = ret * 2 + n % 2
            n /= 2
            count += 1
        return ret

ans = [
    (0,0),
    (43261596,964176192),
]
    
s = Solution()
print s.reverseBits(0)
print s.reverseBits(43261596)