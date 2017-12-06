'''
14. Longest Common Prefix | LeetCode OJ
https://leetcode.com/problems/longest-common-prefix/
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1,len(strs)):
            if len(prefix) == 0:
                return ""
            if len(prefix) > len(strs[i]):
                prefix = prefix[:len(strs[i])]
            for j in range(len(prefix)): #length of prefix is the shortest
                if strs[i][j] != prefix[j]:
                    prefix = prefix[:j]
                    break
        return prefix
    
def test():
    cases = list()
    cases.append( ([], "") )
    cases.append( (["abcdefg"], "abcdefg") )
    cases.append( (["abc","def"], "") )
    cases.append( (["abc","abcde"], "abc") )
    cases.append( (["aa","a"], "a") )
    
    def verify(case):
        s = Solution()
        return s.longestCommonPrefix(case[0]) == case[1]
    
    def run():
        s = Solution()
        return map( s.longestCommonPrefix, [case[0] for case in cases] )
            
    result = filter(verify, cases)
    print run()
    
    return len(result) == len(cases), len(result), len(cases)
    
test()