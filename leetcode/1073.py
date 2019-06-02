class Solution:
    def addBinary(self, arr1, arr2):
        result = []
        c = 0
        while arr1 or arr2:
            a = arr1.pop(-1) if arr1 else 0
            b = arr2.pop(-1) if arr2 else 0
            a = a + b + c
            if a == 3:
                result.insert(0,1) 
                c = 1
            elif a == 2:
                result.insert(0,0) 
                c = 1
            else:
                result.insert(0,a) 
                c = 0
        if c == 1:
            result.insert(0,1)
        return result

    def addNegabinary(self, arr1, arr2):
        result = []
        c = 0
        while arr1 or arr2:
            a = arr1.pop(-1) if arr1 else 0
            b = arr2.pop(-1) if arr2 else 0
            a = a + b - c
            if a == 2:
                result.insert(0,0) 
                c = 1
            else:
                result.insert(0,a) 
                c = 0
        if c == 1:
            result = [1,1] + result
        return result

# 1,0 + 1,0 = 1,1,0,0
s = Solution()
# print(s.addNegabinary(arr1 = [1,1,1,1,1], arr2 = [1,0,1]))
# print(s.addNegabinary(arr1 = [1], arr2 = [1])) # [1,1,0]
print(s.addNegabinary(arr1 = [1,1], arr2 = [1])) # [0]