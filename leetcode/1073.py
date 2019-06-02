class Solution:
    def addNegabinary(self, arr1, arr2):
        result = []
        c = 0
        while arr1 or arr2:
            a = arr1.pop(-1) if arr1 else 0
            b = arr2.pop(-1) if arr2 else 0
            a = a + b + c
            if a >= 2:
                result.insert(0,a-2) 
                c = -1
            elif a == -1:
                result.insert(0,1)
                c = 1
            else:
                result.insert(0,a) 
                c = 0
        if c == -1:
            result = [1,1] + result
        while result and result[0] == 0:
            result.pop(0)
        if not result:
            return [0]
        return result

# 1,0 + 1,0 = 1,1,0,0
s = Solution()
# print(s.addNegabinary(arr1 = [1,1,1,1,1], arr2 = [1,0,1]))
# print(s.addNegabinary(arr1 = [1], arr2 = [1])) # [1,1,0]
# print(s.addNegabinary(arr1 = [1,1], arr2 = [1])) # [0] # WA2
# print(s.addNegabinary(arr1 = [1], arr2 = [1,0,1])) # [1,1,0,1,0] # WA3
print(s.addNegabinary(arr1 = [1,0,1], arr2 = [1,0,1])) # [1,1,1,1,0] # WA4
