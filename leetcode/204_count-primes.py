# 204. Count Primes - LeetCode
# https://leetcode.com/problems/count-primes/description/

# Count the number of prime numbers less than a non-negative number, n.

class Solution(object):
    def countPrimes_MLE(self, n):
        # with input 1500000
        jump_dict = {}
        count = 0
        if n < 3:
            return 0
        for i in range(2,n):
            if jump_dict.has_key(i):
                continue
            else:
                count += 1
                for j in range(i,n,i):
                    jump_dict.update({j:True})
        return count
        
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        lst = [ 0 for i in xrange(n) ]
        count = 0
        for i in xrange(2,n):
            if lst[i] == 1:
                continue
            else:
                count += 1
                for j in xrange(i,n,i):
                    lst[j] = 1
        return count
    
s = Solution()
ans = [
    (0,0),
    (1,0),
    (2,0),
    (3,1),
    (50,15),
    (1500000,114155)
]

for i in ans:
    r = s.countPrimes(i[0])
    print r, r == i[1]