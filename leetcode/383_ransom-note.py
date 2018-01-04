# 383. Ransom Note - LeetCode
# https://leetcode.com/problems/ransom-note/description/

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = defaultdict(int)
        for c in magazine:
            d[c] += 1
        for c in ransomNote:
            if d[c] > 0:
                d[c] -= 1
            else:
                return False
        return True

ans = [
    ("a","b",False),
    ("aa","ab",False),
    ("aa","aab",True),
    ("a"*40,"a"*39,False),
    ("a"*40,"a"*40,True),
]

s = Solution()
for i in ans:
    r = s.canConstruct(i[0],i[1])
    print r, "O" if r == i[2] else "X"