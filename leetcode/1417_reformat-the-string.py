# 1417. Reformat The String - LeetCode
# https://leetcode.com/problems/reformat-the-string/

class Solution:
    def reformat(self, s: str) -> str:
        ret = ""
        alphabets = []
        numbers = []
        
        for c in s:
            if c.isdigit():
                numbers.append(c)
            if c.isalpha():
                alphabets.append(c)
        if abs(len(alphabets)-len(numbers)) > 1:
            return ""
        
        long_seq, short_seq = (alphabets, numbers) if len(alphabets) > len(numbers) else (numbers, alphabets)

        while short_seq:
            ret += long_seq.pop(0)
            ret += short_seq.pop(0)
        
        if long_seq:
            ret += long_seq.pop(0)

        return ret

sl = Solution()
# s = "a0b1c2"
# s = "leetcode"
# s = "1229857369"
s = "covid2019"
# s = "ab123"
ret = sl.reformat(s)
print(ret)
