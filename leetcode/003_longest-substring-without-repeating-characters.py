# 3. Longest Substring Without Repeating Characters - LeetCode
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# class Solution(object):
#     def lengthOfLongestSubstring_TLE(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) < 2: # WA1
#             return len(s)
#         max_length = 0
#         i = 0
#         while i < len(s) - max_length:
#             d = dict()
#             j = i + 1
#             d.update({s[i]:True})
#             current_max = 1
#             while j < len(s):
#                 if d.has_key(s[j]):
#                     break
#                 else:
#                     d.update({s[j]:True})
#                     current_max += 1
#                 j += 1
#             max_length = max( current_max, max_length )
#             i += 1
#         return max_length
#         # return max_length # WA2

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2: # WA1
            return len(s)
        d = {}
        start = 0
        end = 0
        max_length = 0
        for c in s:
            while d.has_key(c):
                del d[s[start]]
                start += 1
            d.update({c:True})
            end += 1
            max_length = max( max_length, end - start )
        return max_length
                
ans = [
    ("",0),
    ("c",1), # WA1
    ("au",2), # WA2
    ("abcabcbb",3), # abc
    ("bbbbb",1), # b
    ("pwwkew",3) # wke
]

s = Solution()
for i in ans:
    r = s.lengthOfLongestSubstring(i[0])
    print r, "O" if r == i[1] else "X"

# time optimization
%timeit -n40 s.lengthOfLongestSubstring([chr(50+(i%50)) for i in range(1000)])
# 40 loops, best of 3: 1.12 ms per loop

# %timeit -n100 s.lengthOfLongestSubstring_TLE([chr(50+(i%50)) for i in range(1000)])
# 100 loops, best of 3: 30.9 ms per loop