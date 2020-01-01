#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#

from typing import List

# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        m, n = len(board), len(board[0])

        def dfs(r, c):
            if r >= m or c >= n:
                return False
            if board[r][c] == "X":
                dfs(r+1, c)
                dfs(r, c+1)
                board[r][c] = '.'
                return True
            else:
                return False

        count = 0
        for r in range(len(board)):
            for c in range(len(board[r])):
                if dfs(r, c):
                    count += 1
        return count


# @lc code=end
s = Solution()
board = """
X..X
.X.X
.X..
"""
board = [ list(i) for i in board.split("\n")[1:-1] ]
ret = s.countBattleships(board)
print(ret)