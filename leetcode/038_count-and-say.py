# 38. Count and Say - LeetCode
# https://leetcode.com/problems/count-and-say/description/

# Example 1:
# Input: 1
# Output: "1"
    
# Example 2:
# Input: 4
# Output: "1211"

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        i = 1
        while i < n:
            j = 0
            new_res = ""
            while j < len(res):
                k = 1
                if j == len(res) - 1:
                    new_res += "1" + res[j]
                    break
                while k <= len(res) - j:
                    if j+k < len(res) and res[j+k] == res[j]:
                        k += 1
                    else:
                        new_res += str(k) + res[j]
                        j += k
                        break
            res = new_res
            i += 1
        return res
        
        
s = Solution()

pairs = [ (1,"1"),
         (2,"11"),
         (3,"21"),
         (4,"1211"),
         (5,"111221"),
         (6,"312211"),
         (11,"11131221133112132113212221") ]

for i in pairs:
    print s.countAndSay(i[0]), i[1] == s.countAndSay(i[0])