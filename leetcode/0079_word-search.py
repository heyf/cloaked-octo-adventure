#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

from typing import List

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(i,j,word_idx):
            if word_idx == len(word):
                return True
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if board[i][j] != word[word_idx]:
                return False
            else:
                c, board[i][j] = board[i][j], "#"
                res = search(i+1,j,word_idx+1) or search(i,j+1,word_idx+1) or search(i-1,j,word_idx+1) or search(i,j-1,word_idx+1)
                board[i][j] = c
                return res

        if not board and not board[0]:
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if search(i,j,0):
                    return True
        return False

# @lc code=end
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

# word = "ABCCED"
# word = "SEE"
word = "ABCB"

s = Solution()
print(s.exist(board, word))