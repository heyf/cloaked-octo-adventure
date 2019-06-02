# 1048. Longest String Chain - LeetCode Contest
# https://leetcode.com/contest/weekly-contest-137/problems/longest-string-chain/

# 用哈希表，保存当前词的最长链

class Solution:
    def longestStrChain(self, words) -> int:
        current_max = 1
        max_dict = {}
        words = sorted(words,key=lambda x: len(x))
        for word in words:
            max_dict[word] = 1
            for idx in range(len(word)):
                minus_word = word[:idx]+word[1+idx:]
                if max_dict.get(minus_word):
                    max_dict[word] = max(max_dict[word],max_dict[minus_word]+1)
                    current_max = max(max_dict[word],current_max)
        return current_max

s = Solution()
print(s.longestStrChain(["a","b","ba","bca","bda","bdca"]))