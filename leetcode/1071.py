# WA: 
# 1 "TAUXXTAUXXTAUXXTAUXXTAUXX"
# 2 "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
# "TAUXX"
# 引入了新的 loop
# class Solution:
#     def gcdOfStrings(self, str1, str2) -> str:
#         s = str1 + str2
#         for n in range(len(s) // 2,0,-1):
#             if len(s) % n > 0:
#                 continue
#             # check repeat
#             for i in range(n,len(s)):
#                 if s[i] != s[i%n]:
#                     break
#             else:
#                 return s[:n]
#         return ""

class Solution:
    def gcdOfStrings(self, str1, str2) -> str:
        max_n = min(len(str1),len(str2))
        for n in range(max_n,0,-1):
            if len(str1) % n > 0 or len(str2) % n > 0:
                continue
            # check repeat
            for i in range(n,len(str1)):
                if str1[i] != str1[i%n]:
                    break
            else:
                for i in range(len(str2)):
                    if str2[i] != str1[i%n]:
                        break
                else:
                    return str1[:n]
        return ""

s = Solution()
# print(s.gcdOfStrings("ABABAB","ABAB"))
# print(s.gcdOfStrings("ABCABC","ABC"))
print(s.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX","TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
