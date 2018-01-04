# 387. First Unique Character in a String - LeetCode
# https://leetcode.com/problems/first-unique-character-in-a-string/description/

# Given a string, find the first non-repeating character in it and return it's index. 
# If it doesn't exist, return -1.

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        l = []
        for i in range(len(s)):
            if d.has_key(s[i]):
                l[d[s[i]]] = False
                l.append(False)
            else:
                d[s[i]] = i
                l.append(True)
        for i in range(len(s)):
            if l[i]:
                return i
        return -1
        
ans = [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("",-1),
    ("a",0),
    ("aa",-1),
    ("aabbccdd",-1),
]
s = Solution()
for i in ans:
    r = s.firstUniqChar(i[0])
    print r, r == i[1]