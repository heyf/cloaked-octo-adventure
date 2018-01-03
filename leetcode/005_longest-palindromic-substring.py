# 5. Longest Palindromic Substring - LeetCode
# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution(object):        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = "#" + "#".join(s) + "#"
        def check_palindrome(start,end):
            if start < 0 or end >= len(s):
                return False
            while end > start:
                if s[start] != s[end]:
                    return False
                end -= 1
                start += 1
            return True
        odd_max = 1
        odd_start = 0
        odd_end = 0
        for i in xrange(len(s)-1):
            if i - odd_max < 0 or i + odd_max > len(s):
                continue
            if check_palindrome(i-odd_max,i+odd_max): # odd
                start = i - odd_max
                end = i + odd_max
                while start >= 0 and end < len(s):
                    if s[start] == s[end]:
                        odd_max += 1
                        odd_start = start
                        odd_end = end
                    else:
                        break
                    start -= 1
                    end += 1
        return s[odd_start:odd_end+1].replace("#","")

ans = [
    ("",[""]),
    ("a",["a"]),
    ("ab",["a","b"]),
    ("babad",["bab","aba"]),
    ("cbbd",["bb"]),
    ("abcd",["a","b","c","d"]),
    ("abbbc",["bbb"]),
    ("abbbbc",["bbbb"]),
    ("abb",["bb"]),
]

s = Solution()
for i in ans:
    r = s.longestPalindrome_brutal(i[0])
    print r, r in i[1]