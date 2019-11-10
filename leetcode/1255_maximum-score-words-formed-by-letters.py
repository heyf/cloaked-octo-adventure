# Maximum Score Words Formed by Letters - LeetCode Contest
# https://leetcode.com/contest/weekly-contest-162/problems/maximum-score-words-formed-by-letters/

from typing import List
from functools import lru_cache

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        class Word():
            def __init__(self, word):
                word_list = [ 0 for s in score ]
                word_score = 0
                for char in word:
                    idx = ord(char) - ord("a")
                    word_list[idx] += 1
                    word_score += score[idx]

                # public member
                self.word_list = word_list
                self.score = word_score

            @lru_cache(maxsize=None)
            def check_available(self, letters_left):
                valid_letters_left = list(letters_left)
                for idx, count in enumerate(self.word_list):
                    if count > valid_letters_left[idx]:
                        return False, letters_left
                    else:
                        valid_letters_left[idx] -= count
                return True, tuple(valid_letters_left)
        
        word_letter_list = [ Word(word) for word in words ]

        @lru_cache(maxsize=None)
        def helper(idx, letters_left):
            if idx < 0 or idx >= len(word_letter_list):
                return 0
            word = word_letter_list[idx]
            valid, valid_letters_left = word.check_available(letters_left)
            sum_score = 0
            if valid:
                sum_score = helper(idx-1, valid_letters_left) + word.score
            without_sum_score = helper(idx-1, letters_left)
            sum_score = max(sum_score, without_sum_score)
            return sum_score

        letters_left = [ 0 for s in score]
        for char in letters:
            idx = ord(char) -  ord('a')
            letters_left[idx] += 1

        global_max = 0
        for idx in range(len((word_letter_list))):
            global_max = max( global_max, helper(idx, tuple(letters_left)) )

        return global_max

# Example 1: 23
# words = ["dog","cat","dad","good"]
# letters = ["a","a","c","d","d","d","g","o","o"]
# score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

# Example 2: 27
# words = ["xxxz","ax","bx","cx"]
# letters = ["z","a","b","c","x","x","x"]
# score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]

# Example 3: 0
# words = ["leetcode"]
# letters = ["l","e","t","c","o","d"]
# score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]

# # WA1: Expected: 51
# words = ["add","dda","bb","ba","add"]
# letters = ["a","a","a","a","b","b","b","b","c","c","c","c","c","d","d","d"]
# score = [3,9,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# words[i] cannot be used two or more times

# WA2: Expected: 27
words = ["bdabd","bec","cbeb","bceb","dde"]
letters = ["a","a","a","b","b","b","b","c","c","c","d","d","e","e"]
score =[10,2,6,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

s = Solution()
ret = s.maxScoreWords(words, letters, score)
print(ret)