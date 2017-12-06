# 28. Implement strStr() - LeetCode
# https://leetcode.com/problems/implement-strstr/description/

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
    
# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        while i <= len(haystack) - len(needle):
            j = 0
            while j < len(needle):
                if haystack[i+j] == needle[j]:
                    j += 1
                else:
                    break
            if j == len(needle):
                return i
            i += 1
        return -1
            

s = Solution()

haystack = "hello"
needle = "o"
print s.strStr(haystack,needle)