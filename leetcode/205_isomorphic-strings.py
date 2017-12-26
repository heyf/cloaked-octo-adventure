# 205. Isomorphic Strings - LeetCode
# https://leetcode.com/problems/isomorphic-strings/description/
    
# Given "egg", "add", return true.
# Given "foo", "bar", return false.
# Given "paper", "title", return true.
    
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st = dict()
        ts = dict()
        for i in range(len(s)):
            if st.has_key(s[i]) and st[s[i]] != t[i]:
                return False
            elif ts.has_key(t[i]) and ts[t[i]] != s[i]:
                return False
            else:
                st.update({s[i]:t[i]})
                ts.update({t[i]:s[i]})
        return True
                

ans = [
    ( "egg", "add", True ),
    ( "foo", "bar", False),
    ( "paper", "title", True),
    ( "aa", "ab", False ),
    ( "ab", "aa", False ), # WA: 1
]

s = Solution()
for i in ans:
    r = s.isIsomorphic(i[0],i[1])
    print r, "O" if r == i[2] else "X"