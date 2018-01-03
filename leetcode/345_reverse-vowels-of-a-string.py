# 345. Reverse Vowels of a String - LeetCode
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {
            "a": True,
            "e": True,
            "i": True,
            "o": True,
            "u": True,
            "A": True,
            "E": True,
            "I": True,
            "O": True,
            "U": True,
        }
        s = list(s)
        start = 0
        end = len(s) - 1
        while end > start:
            if vowels.has_key(s[start]) and not vowels.has_key(s[end]):
                end -= 1
                continue
            elif vowels.has_key(s[end]) and not vowels.has_key(s[start]):
                start += 1
                continue
            elif vowels.has_key(s[end]) and vowels.has_key(s[start]):
                t = s[end]
                s[end] = s[start]
                s[start] = t
            end -= 1
            start += 1
        return "".join(s)
        
ans = [
    ("hello","holle"),
    ("a","a"),
    ("",""),
    ("leetcode","leotcede"),
]
s = Solution()
for i in ans:
    r = s.reverseVowels(i[0])
    print r, r == i[1]