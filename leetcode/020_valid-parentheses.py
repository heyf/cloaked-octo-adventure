# 20. Valid Parentheses - LeetCode
# https://leetcode.com/problems/valid-parentheses/description/
# '(', ')', '{', '}', '[' and ']'

# stack base
# Submit 1: "]" edge case
# Submit 2: "[(({})}]" WA
## Logic Failed: ord("(") - ord("}") = -85 < 3
    # print ord("(") - ord(")")
    # print ord("(") - ord("]") x
    # print ord("(") - ord("}") x
    # print ord("[") - ord(")") x
    # print ord("[") - ord("]") 
    # print ord("[") - ord("}") x
    # print ord("{") - ord(")") x
    # print ord("{") - ord("]") x
    # print ord("{") - ord("}")
# Submit 3: 25 mins, AC

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for i in s:
        if i in [ "(", "[", "{" ]:
            stack.append(ord(i))
        if i in [ ")", "]", "}" ]:
            if len(stack) == 0:
                return False
            res = ord(i) - stack[-1]
            if res > 0 and res < 3:
                stack.pop(-1)
            else:
                return False
    if len(stack) != 0:
        return False
    else:
        return True
    
isValid("()")