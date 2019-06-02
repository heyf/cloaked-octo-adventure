# 1047. Remove All Adjacent Duplicates In String - LeetCode Contest
# https://leetcode.com/contest/weekly-contest-137/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        while i < len(S) - 1:
            if S[i] == S[i+1]:
                S = S[:i] + S[i+2:]
                if i > 0:
                    i -= 1
            else:
                i += 1
        return S

s = Solution()
print(s.removeDuplicates("abbaa"))