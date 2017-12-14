# 125. Valid Palindrome - LeetCode
# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        lst = []
        for i in range(len(s)):
            j = ord(s[i])
            if j < 58 and j > 47:
                lst.append(j)
            elif j < 123 and j > 96:
                lst.append(j)
            elif j > 64 and j < 91:
                lst.append(j+32)
        i = 0
        j = len(lst) - 1
        while i < j:
            if lst[i] != lst[j]:
                return False
            i += 1
            j -= 1
        return True
    
s = Solution()
pairs = [
    ("A man, a plan, a canal: Panama",True),
    ("race a car", False),
    ("0P", False),
]
for i in pairs:
    res = s.isPalindrome(i[0])
    print(i[0], res,"V" if res==i[1] else "X")