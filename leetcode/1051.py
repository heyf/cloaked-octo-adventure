class Solution:
    def heightChecker(self, heights) -> int:
        old_heights = heights.copy()
        heights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if old_heights[i] != heights[i]:
                count += 1
        return count

# WA
# class Solution:
#     def heightChecker(self, heights) -> int:
#         count = 0
#         for i in range(len(heights)):
#             local_min = i
#             for j in range(i+1,len(heights)):
#                 if heights[j] < heights[local_min]:
#                     local_min = j
#             if local_min != i:
#                 heights[local_min], heights[i] = heights[i], heights[local_min]
#                 count += 1
#         if count > 0:
#             count += 1
#         return count

s = Solution()
print(s.heightChecker([1,1,4,2,1,3])) # 3
print(s.heightChecker([2,1,2,1,1,2,2,1])) # 4